##synset = collection of synonymous words, or 'lemmas'

import nltk
from nltk.corpus import wordnet as wn

motorcar = wn.synset('car.n.01')
##hyponyms are more specific concepts (i.e., ambulance for 'car')
types_of_motorcar = motorcar.hyponyms()
print types_of_motorcar[26]

## line 10 does NOT work!
#sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas])
## --- Working version of line 10 ---
## specific instances (i.e., hyponynms of 'motorcar')
print sorted(lemma.name() for synset in types_of_motorcar for lemma in
            synset.lemmas())
print "-----------#------------"
print motorcar.hypernyms()
paths = motorcar.hypernym_paths()
print len(paths)
##wheeled_vehicle.n.01 as container
x = [synset.name for synset in paths[0]]
print x
##wheeled_vehicle.n.01 as vehicle and conveyance
y = [synset.name for synset in paths[1]]
print y

##launches wordnet in browser
print nltk.app.wordnet()
