from __future__ import division
from nltk.book import *

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 100 * count / total

print lexical_diversity(text5)
print percentage(5, 46542)