#!/usr/bin/python3
#parse.py

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

# OPENS URL AND SAVES OUTPUT AS VARIABLE URL_REQUEST
url = 'http://192.168.235.68:8080/crawling'
url_request = urlopen(url)

# READS URL_REQUEST AND USES BEAUTIFUL SOUP TO TIDY IT UP.
page = url_request.read()
soup = BeautifulSoup(page, features="html.parser")

# GET_TEXT EXTRACTS ALL TEXT/DIRECTORY PATHS AND THEN "\n", strip=True REMOVES ANY BLANK LINES.
sort_dirs = soup.get_text("\n", strip=True)

# DIRECTORIES.TXT IS CREATED TO A CREATE A READABLE/PARSABLE OBJECT FROM SORT_DIRS OUTPUT.
with open('directories.txt', 'w') as f:
	f.write(sort_dirs)
	
# DIRECTORIES.TXT IS OPENED AND READ LINE BY LINE AND PARSED INTO URLOPEN AND THE PROCESS ABOVE IS REPEATED.
dirs = open('directories.txt', 'r')

for line in dirs:
	url2 = urlopen(url + "/" + line)
	page = url2.read()
	soup = BeautifulSoup(page, features="html.parser")
	print(soup)
	
