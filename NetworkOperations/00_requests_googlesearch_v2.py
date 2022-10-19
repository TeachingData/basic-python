"""
This script is to show the main factors of requests and how to use it with an HTML Parser
HTML Parser to use is BeutifulSoup: one of the best xml and html parsers

This version adds better command-line arguement handling.
"""

import sys, argparse
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# version number TODO: Load version library
VERSION = 2.02

# main sites to search with query strings
# will have to make this a full dispatch table to custom functions later
sites = {
    "google": "www.google.com/search?q=",
    "amazon": "www.amazon.com/s?k=",
    "wikipedia": "en.wikipedia.org/wiki/",
    "wiki": "en.wikipedia.org/wiki/",
    "gutenberg": "www.gutenberg.org/ebooks/search/?submit_search=Go%21&query="
}


def init() -> str:
    sysargs = argparse.ArgumentParser(description="Loads passed url to file after intial cleaning (munging).")
    sysargs.add_argument("-v", "--version", action="version", version=f"Current version is {VERSION}")
    sysargs.add_argument("-s", "--site", help="The site to search (google, wikipedia, gutenberg, amazon)")
    sysargs.add_argument("-q", "--query", help="The term(s) to search for.")
    args = sysargs.parse_args()
    return build_url(args.site, args.query)


def build_url(site, searchterm):
    """

    :param site: The site to be searched from choices provided
    :param searchterm: The term to search for
    :return: the fully built query string
    """
    site = site.lower()
    if site not in sites:
        return ""

    if site == "wikipedia" or site == "wiki":
        searchterm = "_".join(searchterm.split())
    else:
        searchterm = "+".join(searchterm.split())
    return f'https://{sites[site]}{searchterm}'


def get_response(uri):
    # search get and return a response from the url provided
    # Add https to urls without protocol with layer
    if not uri.lower().startswith('http'):
        uri = f'https://{uri}'

    # Gets website url and provides response
    # If error - exits with exception
    try:
        response = requests.get(uri)
        response.raise_for_status()
    except HTTPError as httperr:
        print(f'HTTP error: {httperr}')
        sys.exit(1)
    except Exception as err:
        print(f"Something went really wrong!: {err}")
        sys.exit(1)

    return response.text


if __name__ == '__main__':
    url = init()
    # Open our page with beautiful soup to parse it and find information

    if url:
        soup = BeautifulSoup(get_response(url), 'html.parser')

        # The names (not links) ended up being all the header 3 tags so load them
        # Then we will pull the divs (div tags had the string we needed) and each one's string
        # print to console so this can be redirected or piped to another program
        # TODO: Next version create a dispatch table or at least multiple functions for each url
        # google
        for link in soup.findAll("h3"):
            print(link.div.string)
        # wikipedia Florida Gulf Coast
        #for link in soup.find_all("li"):
            # if "Florida" in link.text: print(link.text)
