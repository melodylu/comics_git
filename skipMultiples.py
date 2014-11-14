#!/usr/bin/python
# Written in Python with a whole lot of quick google searches. The for loop took 90 seconds to type out. Getting the library BeautifulSoup to correctly scrape that quotes I wanted off of KingJamesProgramming took 4 hours. Arg.

def skipMultiples():
	from bs4 import BeautifulSoup
	import requests



	url = 'http://kingjamesprogramming.tumblr.com/'

	r = requests.get(url)
	soup = BeautifulSoup(r.text)

	quoteStack = []

	for tag in soup.find_all("blockquote"):
		quote = tag.get_text().strip()
		quoteStack.append(quote)




	for i in range(1, 51):
		if i%7 != 0:
			 print "This has worked",i,"times, praise be"
		else:
			print quoteStack[i/7]


	print  "\n""        -- http://kingjamesprogramming.tumblr.com/""\n"
	return

skipMultiples();



#  just plain for loop below


# for i in range(1, 51):
# 	if i%7 != 0:
# 		 print "This has worked",i,"times, praise be"
# 		 i = i + 1
# 	else:
# 		print "The problem arises from the fact that it is possible to show that the value for b is to be cleansed"
