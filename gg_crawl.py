#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import time


url = 'http://www.girlgeniusonline.com/comic.php?date=20021104'

r = requests.get(url)
soup = BeautifulSoup(r.text)

images = []

for i in range(2):
	imageObject = soup.find("img", attrs={'alt': 'The Next Comic'})
	images.append(imageObject.parent.get('href'))
	url = images[-1]
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	time.sleep(4)

print "\n".join(images)


# - start with the premodial strip
# - get the next comic link
# - stick into list
# - do this 20 times

# - print list
