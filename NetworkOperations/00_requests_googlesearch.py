"""
This script is to show the main factors of requests and how to use it with an HTML Parser
HTML Parser to use is BeutifulSoup: one of the best xml and html parsers
"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys

# to install Beautiful Soup: File-->Settings-->Project Interpreter and "add package"

if __name__ == '__main__':
    for url in sys.argv[1:]:
        # Add https to urls without protocol with layer
        if not url.lower().startswith('http'):
            url = f'https://{url}'

        # Gets website url and provides response
        # If error - exits with exception
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as httperr:
            print(f'HTTP error: {httperr}')
            sys.exit(1)
        except Exception as err:
            print(f"Something went really wrong!: {err}")
            sys.exit(1)

        # Open our page with beutiful soup to parse it and find information
        soup = BeautifulSoup(response.text, 'html.parser')

        # The names (not links) ended up being all the header 3 tags so load them
        # Then we will pull the divs (div tags had the string we needed) and each one's string
        # print to console so this can be redirected or piped to another program
        for link in soup.findAll("h3"):
            print(link.div.string)
