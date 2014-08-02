import sys
import json
from bs4 import BeautifulSoup
import urllib

def main():
	query = sys.argv[1].decode('utf-8')
	theURL = "http://www.perseus.tufts.edu/hopper/morph?l=" + query + "&la=latin"

	html = urllib.urlopen(theURL).read()
	soup = BeautifulSoup(html)

	parse_results = soup.find('div', {"id" : "main_col"})
	parse_items = parse_results.findAll('div', {"class" : "analysis"})

	_data = []
	for item in parse_items:
		lemma = item.h4.string
		definition = item.span.string.strip()
		parsings = item.table.findAll('td', {"class" : None})
		parsing_data = []
		for x in parsings:
			if x.get('style') == None:
				parsing = x.string
				parsing_data.append(parsing)
		_data.append([lemma, definition, parsing_data])
	print json.dumps(_data, sort_keys=True, indent=4, separators=(',', ': ')).encode('utf-8')
 
if __name__ == '__main__':
    main()