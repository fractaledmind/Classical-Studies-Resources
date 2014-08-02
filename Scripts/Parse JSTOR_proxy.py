import cookielib
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import json

query = 'herodotus'

theURL = "http://proxy.library.upenn.edu:2165/action/doBasicSearch?Query=" + query + "&acc=on&wc=on&fc=off"



# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'JSTORTesting')]

# Install our opener (note that this changes the global opener to the one we just made, but you can also just call opener.open() if you want)
urllib2.install_opener(opener)

# The action/ target from the form
authentication_url = "https://proxy.library.upenn.edu/login"

# Input parameters we are going to send
payload = {
  'url': "http://www.jstor.org/action/doBasicSearch?Query=herodotus&amp;acc=on&amp;wc=on&amp;fc=off",
  'user': 'margheim',
  'pass': 'Dr.Horace19'
  }

# Use urllib to encode the payload
data = urllib.urlencode(payload)

# Build our Request object (supplying 'data' makes it a POST)
req = urllib2.Request(authentication_url, data)

# Make the request and read the response
resp = urllib2.urlopen(req)
contents = resp.read()
print contents
soup = BeautifulSoup(contents)
results = soup.find('fieldset', {"class" : "citeList results"})
cite_items = results.findAll('div', {"class" : "cite"})

_data = []
for item in cite_items:
	title = item.find('div', {"class" : "title"})
	author = item.find('div', {"class" : "author"}).a
	bib = item.find('div', {"class" : "srcInfo"})
	bib_data = re.sub("<.*?>", "", str(bib))
	pdf_link = item.find('a', {"class" : "pdflink"}).get('href')
	_data.append([title, author, bib_data, pdf_link])
print _data
#print json.dumps(_data, sort_keys=True, indent=4, separators=(',', ': '))

