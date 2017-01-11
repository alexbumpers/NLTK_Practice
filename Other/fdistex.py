from nltk.book import *

fdist1 = FreqDist(text6)
print fdist1 #print f distribution (samples out of outcomes)
print "-----------------"

vocabulary1 = fdist1.keys() #for .keys, you can use "for key in x"
print vocabulary1[:50] #prints 50 distinct types in text
print "---------------------"
print fdist1['grail'] #samples of 'grail' in monty python
#cumulative frequency is the total frequencies SO FAR in a FreqDist
#cumulative frequency plot of 50 most used words in Monty Python
print fdist1.hapaxes()
print fdist1.plot(50, cumulative=True)