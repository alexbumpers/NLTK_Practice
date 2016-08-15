from nltk.book import *

#imports bigram module (see NLTK docs)
from nltk.util import bigrams 

#prints a list of word pairs - use list() to get list output
print list(bigrams(['more', 'is', 'said', 'than', 'done']))

#prints bigrams from textX
print text4.collocations()




#prints lengths of words in text1
print [len(w) for w in text1]

#defines variable to show frequency of how often each word occurs
fdist = FreqDist([len(w) for w in text1])
print fdist

#prints distribution, each item correspanding to word token in text
print "fdist.keys()"
print fdist.keys()

#freq of diff lengths of words
print "fdist.items()"
print fdist.items()

#most frequent word length
print "fdist.max()"
print fdist.max()

#how many times it occurs
print fdist[3]

#freq of given sample (3)
print "fdist.freq(3)"
print fdist.freq(3)
