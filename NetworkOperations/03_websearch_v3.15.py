"""
This script is to show the main factors of requests and how to use it with an HTML Parser
HTML Parser to use is BeutifulSoup: one of the best xml and html parsers

This version adds error handling and a research after finding a link but shows how fragile webscraping can be.
Hence - it only works for one search term using Google - version 3.5 will remove some of this fragility.
You can run it in the background with a command like: (windows/powershell)
 start PathtoEXE\python.exe -ArgumentList ("websearch.py", "-s", "google", "-q", "fgcu") -NoNewWindow
                -RedirectStandardOutput google_fgcu.txt
"""

import sys, argparse
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# version number TODO: Load version library
# and functions for dispatch table
VERSION = 3.04


def search_google(searchterms):
    """
    Searches google for a search term and returns the first link.

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "+".join(searchterms.split())
    url = f'https://www.google.com/search?q={searchterms}'
    soup = BeautifulSoup(get_response(url), 'html.parser')

    for link in soup.findAll("a", href=True):
        if link.h3:
            print(link['href'][7:])
            return link['href'][7:]


def search_amazon(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "+".join(searchterms.split())
    url = f'https://www.amazon.com/s?k={searchterms}'

    soup = BeautifulSoup(get_response(url), 'html.parser')
    for link in soup.find_all("p"):
        print(link.text)
        return link.text


def search_wiki(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "_".join(searchterms.split())
    # real search = https://en.wikipedia.org/w/index.php?fulltext=1&search={searchterm}%20&title=Special%3ASearch&ns0=1
    url = f'https://en.wikipedia.org/wiki/{searchterms}_(disambiguation)'

    soup = BeautifulSoup(get_response(url), 'html.parser')
    for link in soup.find_all("li"):
        print(link.text)
        return link.text


def search_books(searchterms):
    """

    :param searchterms: The term to search for
    :return: the fully built query string
    """
    searchterms = "+".join(searchterms.split())
    url = f'https://www.gutenberg.org/ebooks/search/?submit_search=Go%21&query={searchterms}'

    soup = BeautifulSoup(get_response(url), 'html.parser')
    for link in soup.find_all("p"):
        print(link.text)
        return link.text

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
    print(get_response(url))
    # Open our page with beautiful soup to parse it and find information

    # The names (not links) ended up being all the header 3 tags so load them
    # Then we will pull the divs (div tags had the string we needed) and each one's string
    # print to console so this can be redirected or piped to another program
    # TODO: Next version create a dispatch table or at least multiple functions for each url
