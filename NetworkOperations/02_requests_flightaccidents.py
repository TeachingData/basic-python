# very simple script to download and save a simple text file then create a csv from it
# Typically I would have these in classes but let us start small (and using 2 libraries)
# This also is meant to show downloading multiple files
from urllib import request
import requests
# The main library we will use is requests but I want to show a little bit of urllib as well
from bs4 import BeautifulSoup


# to install Beautiful Soup: File-->Settings-->Project Interpreter and "add package"

def get_files() -> set:
    _filenames = set()

    page = requests.get("https://av-info.faa.gov/dd_sublevel.asp?Folder=%5CAID")
    # print(page.text) # hard to read ain't it?
    # we just need stuff in the TDs anyway so:
    soup = BeautifulSoup(page.text, 'html.parser')
    # can try td, a
    for csv in soup.find_all('a'):
        # cool this prints the text now we just need to filter
        # so we only want txt files which begin in a
        if 'txt' in csv.text and csv.text[0] == 'a':
            _filenames.add(csv.text)
    return _filenames


def get_file(file: str = "e2020_25"):
    # filename changes so we will add that manually (eventually as argument)
    base_url = "https://av-info.faa.gov/data/AID/tab/"

    # now we download and decode it - if it was a binary file we'd just read
    # binary meaning pdf, mp3, or those zips
    with request.urlopen(base_url + file + ".txt") as textfile:
        accidents = textfile.read().decode('utf-8')

    # SHHH...this is a csv - its just tab delimited not comma (,)
    # It has a bunch of extra lines (think linux vs Windows)...possibly so let's fix that
    #    By forcing a standard newline and encoding
    with open("./csvs/" + file + ".csv", 'w', newline='', encoding='utf-8') as txt:
        txt.write(accidents)


if __name__ == '__main__':
    # First we need to load all the information into a list or dict
    filenames = get_files()
    print(filenames)

    # TODO: add loop here to call multiple get_file functions by filenames
    # call get_file after we find what pages are there with soup
    # get_file("somefile")
    
    # TODO: Students change this to work with wikipedia pages given in assignment
