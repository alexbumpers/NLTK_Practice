from nltk.book import *

print sent7

#print words in sent7 that are less than four characters
print [w for w in sent7 if len(w) < 4]

#print words in sent7 that are less than or equal to four characters
print [w for w in sent7 if len(w) <= 4]