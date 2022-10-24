"""
This script is to show the main factors of requests and how to use it with an HTML Parser
HTML Parser to use is BeutifulSoup: one of the best xml and html parsers

This version adds a dispatch table for custom function launching and error handling related to it.
"""

import sys, argparse
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# version number TODO: Load version library
# and functions for dispatch table
VERSION = 3.03


def search_google(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "+".join(searchterms.split())
    return f'https://www.google.com/search?q={searchterms}'


def search_amazon(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "+".join(searchterms.split())
    return f'https://www.amazon.com/s?k={searchterms}'


def search_wiki(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "_".join(searchterms.split())
    return f'en.wikipedia.org/wiki/{searchterms}'


def search_books(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "+".join(searchterms.split())
    return f'www.gutenberg.org/ebooks/search/?submit_search=Go%21&query={searchterms}'

# main sites to search with query strings
# will have to make this a full dispatch table to custom functions later
sites = {
    "google": search_google,
    "amazon": search_amazon,
    "wikipedia": search_wiki,
    "wiki": search_wiki,
    "gutenberg": search_books,
    "books": search_books
}


def init() -> str:
    sysargs = argparse.ArgumentParser(description="Loads passed url to file after initial cleaning (munging).")
    sysargs.add_argument("-v", "--version", action="version", version=f"Current version is {VERSION}")
    sysargs.add_argument("-s", "--site", help="The site to search (google, wikipedia, gutenberg, amazon)")
    sysargs.add_argument("-q", "--query", help="The term(s) to search for.")
    args = sysargs.parse_args()

    # check that all arguments were passed
    site = str(args.site).lower()
    try:
        if args.query:
            return sites.get(site)(args.query)
        else:
            print("You must provide both the site (-s,--site) and query string (-q,--q) to use this program.")
            quit(1)
    except (KeyError, TypeError) as ex:
        print("Acceptable sites to search for are: google, wikipedia(wiki), amazon, gutenberg(books)")
        quit(1)


def get_response(uri):
    # search get and return a response from the url provided

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

    soup = BeautifulSoup(get_response(url), 'html.parser')

    # The names (not links) ended up being all the header 3 tags so load them
    # Then we will pull the divs (div tags had the string we needed) and each one's string
    # print to console so this can be redirected or piped to another program
    # TODO: Next version create a dispatch table or at least multiple functions for each url
    # google
    for link in soup.findAll("h3"):
        print(link.div.string)
        # wikipedia Florida Gulf Coast
        # for link in soup.find_all("li"):
        # if "Florida" in link.text: print(link.text)
