# -*- coding= utf-8 -*-
import sys
from bs4 import BeautifulSoup
import urllib
import re


def main():
	query = sys.argv[1].decode('utf-8')
	base = 'http://www.perseus.tufts.edu/hopper/text?doc=' 
	dict = urllib.quote(query)
	url = base + dict
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	_results = soup.find('div', {"class" : "text_container"})
	result = re.sub("<.*?>", "", str(_results))
	res = result.strip()
	print res.encode('utf-8')

if __name__ == '__main__':
	main()
