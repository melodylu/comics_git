#!/usr/bin/python

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

	print "\n".join(quoteStack)
	print "\n",quoteStack[0]
	return
	
skipMultiples();






	# for child in soup.body.article.p.descendants:
	# 	print child,
	# 	print  "\n""        - kingjamesprogramming"



# for q in range(0,2):
# 	quote = soup.body.article.p.contents
# 	print quote
# 	q = q + 1


# for i in range(1, 51):
# 	if i%7 != 0:
# 		 print "This has worked",i,"times, praise be"
# 		 i = i + 1
# 	else:
# 		print "The problem arises from the fact that it is possible to show that the value for b is to be cleansed"




#	quote = soup.find("article", attrs={'class': 'post text'}).get("src")
