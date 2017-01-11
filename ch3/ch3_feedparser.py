from __future__ import division
import nltk, re, pprint
from urllib2 import urlopen
from nltk import word_tokenize
from bs4 import BeautifulSoup
import feedparser

llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print llog['feed']['title']
print len(llog.entries)
post = llog.entries[2]
print post.title

content = post.content[0].value
print content[:70]

raw = BeautifulSoup(content, "lxml").get_text()
print word_tokenize(raw)
