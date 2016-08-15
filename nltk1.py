from nltk.book import *
text1.similar("large") #shows words appearing in similar ranges of context
print "----"
text2.common_contexts(["much", "very"])
text1.concordance("whale") #shows all instances of word + context
