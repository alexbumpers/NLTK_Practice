from nltk.book import *

#-------- Provides informative context about text --------


#defines freqdist variable for text5
fdist5 = FreqDist(text5)
#prints list of words from text5 that are longer than 7 chars (len) and
#occur more than seven times (fdist)
print sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])