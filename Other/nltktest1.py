from __future__ import division
from nltk.book import *

saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is',
          'said', 'than', 'done']
tokens = set(saying) #variable returning the set in the list
tokens = sorted(tokens) #variable sorting list 'saying' in ABC order
print tokens[-2:] #prints the sorted&set list 2 tokens from the end of it