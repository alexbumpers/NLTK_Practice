"""Tokenization is defined as follows: in language processing, breaking up a
string into words and punctuation. Produces a familiar structure to us: a list
of words and punctuation!"""

from __future__ import division
import nltk, re, pprint
from urllib import urlopen

url = "http://www.gutenberg.org/files/2554/2554.txt"
# Opens and reads url
raw = urlopen(url).read()
# Prints type of data, prints length of data, prints first 75 chars in raw
print type(raw)
print len(raw)
print raw[:75]

# Tokenizes raw into characters and punctuation, removing whitespace, etc.
tokens = nltk.word_tokenize(raw)
# Prints type of data in tokens, prints len of tokens, prints first 10 chars
# in tokens
print type(tokens)
print len(tokens)
print tokens[:10]

# Converts tokens from raw into a text we can analyze with NLTK
text = nltk.Text(tokens)
print type(text)
print text[1020:1060]
print text.collocations()

# The find() and rfind() ("reverse find") methodsget the right index values to
# use for slicing the string [1].
print raw.find("PART I")
print raw.rfind("End of Project Gutenberg's Crime")
# We overwrite raw with this slice,
# so now it begins with "PART I" and goes up to (but not including) the phrase
# that marks the end of the content.
raw = raw[5303:1157681]
print raw.find("PART I")
