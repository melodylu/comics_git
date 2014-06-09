#!/usr/bin/python

import os
from bs4 import BeautifulSoup
import requests



def downloadImage(url, currentFileName):
	with open(currentFileName, 'wb') as handle:
	    response = requests.get(url, stream=True)
	    
	    for block in response.iter_content(1024):
	        if not block:
	            break
	        handle.write(block)









url = 'http://www.girlgeniusonline.com/comic.php?date=20021104'

r = requests.get(url)
soup = BeautifulSoup(r.text)

images = [link.get('src') for link in soup.find_all("img", attrs={'alt': 'Comic'})]


print images
currentFileName = os.path.basename(images[0])
print currentFileName




downloadImage(images[0], currentFileName)
