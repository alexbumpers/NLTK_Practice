from __future__ import division
from nltk.book import *

text3
#prints number of tokens in text3
print len(text3) 
#prints number of UNIQUE tokens in text3
print len(sorted(set(text3))) 
#defines variable to print average use of words
avg_each_word = len(text3) / len(sorted(set(text3)))
#prints avg_each_word to shell
print avg_each_word
#prints word count for a specific word to shell
print text3.count("smote")
#percentage that str('a') appears in text4
print 100 * text3.count('a') / len(text4)


print text5.count('lol')

print 100 * text5.count('lol') / len(text5)
