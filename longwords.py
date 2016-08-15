from nltk.book import *

V = set(text1)
#for each word(w) in the vocabulary (w), check if len(w) > 15
long_words = [w for w in V if len(w) > 13]
#prints sorted (ABC) list of words > 13 characters
print sorted(long_words)