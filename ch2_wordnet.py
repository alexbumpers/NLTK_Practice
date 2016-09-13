import nltk
from nltk.corpus import wordnet as wn

print wn.synsets('motorcar')
## ^^^^ synset is a synonym set - a collection of synonymous words (or 'lemmas')
##prints [Synset('car.n.01')] which is the first noun sense of car
print wn.synset('car.n.01').lemma_names
##definition of 'car'
print wn.synset('car.n.01').definition
##example sentence with 'car'
print wn.synset('car.n.01').examples

print wn.synset('car.n.01').lemmas
print '##########'
print wn.lemma('car.n.01.automobile')
print '#-#-#-#-#-#'
print wn.lemma('car.n.01.automobile').synset
print '###---###---###'
print wn.lemma('car.n.01.automobile').name

## --------------###########-------------- ##
print wn.synsets('car')
for synset in wn.synsets('car'):
    print synset.lemma_names
print wn.lemmas('car')
