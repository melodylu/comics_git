#!/usr/bin/python

from bs4 import BeautifulSoup
import requests, time, os

def downloadImage(url, currentFileName):
	with open(currentFileName, 'wb') as handle:
	    response = requests.get(url, stream=True)
	    
	    for block in response.iter_content(1024):
	        if not block:
	            break
	        handle.write(block)


url = 'http://www.girlgeniusonline.com/comic.php?date=20140604'

r = requests.get(url)
soup = BeautifulSoup(r.text)

pagesVisited = []

for i in range(900):
	pageObject = soup.find("a", attrs={'title': 'The Next Comic'})
	pagesVisited.append(pageObject.get('href'))
	url = pagesVisited[-1]
	
	imageSrc = soup.find("img", attrs={'alt': 'Comic'}).get("src")
	currentFileName = os.path.basename(imageSrc)
	downloadImage(imageSrc, currentFileName)
	
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	
	time.sleep(1)

# print "\n".join(pagesVisited)