from __future__ import division
import nltk, re, pprint
from urllib2 import urlopen
from nltk import word_tokenize
from bs4 import BeautifulSoup


url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read().decode('utf8')
print html[:60]
print html

# Tokenizes HTML from the given url and print it all to console
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
print tokens

# Overrides tokens variable to only look through tokens at indices 110:390
tokens = tokens[110:390]
text = nltk.Text(tokens)
# Finds concordance of 'gene' in text. I.e., appearance of 'gene' in context
print text.concordance('gene')
