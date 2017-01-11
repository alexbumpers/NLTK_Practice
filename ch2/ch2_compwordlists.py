## Swadesh wordlists are comparative wordlists (i.e., tabular lexicons), lists
## of ~200 common words in several languages. These are identified using an
## ISO 639 two-letter code.
import nltk
from nltk.corpus import swadesh

##swadesh fileids (i.e., 2 letter ISO 639 codes for different languages)
print swadesh.fileids()

#200 common words in English
print swadesh.words('en')

fr2en = swadesh.entries(['fr', 'en'])
print fr2en

translate = dict(fr2en)
print translate['vous']

languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
for i in [139, 140, 141, 142]:
    print swadesh.entries(languages)[i]
print "-----"
from nltk.corpus import toolbox
print toolbox.entries('rotokas.dic')
