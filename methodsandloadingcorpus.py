import nltk
from nltk.corpus import gutenberg

#gutenberg.fileids()
#raw = gutenberg.raw("burgess-busterbrown.txt")
##prints characters 1-19
#print raw[1:19]

#words = gutenberg.words("burgess-busterbrown.txt")
##prints words 1-5
#print words[1:5]

#sents = gutenberg.sents("burgess-busterbrown.txt")
##prints sentences 1-3
#print sents[1:3]

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
##prints file names
print wordlists.fileids()
##prints words from file named 'connectives'
print wordlists.words('connectives')

from nltk.corpus import BracketParseCorpusReader

corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
file_pattern = r".*/wsj_.*\.mrg"
ptb = BracketParseCorpusReader(corpus_root, file_pattern)
ptb.fileids()
print len(ptb.sents())
