## --------- BASIC CORPUS FUNCTIONALITY FOR NLTK -----------
## FOR HELP SEE: help(nltk.corpus.reader) and nltk.org/howto

#FILES OF CORPUS
fileids()

#FILES OF CORPUS CORRESPONDING TO THESE CATEGORIES
fileids([categories])

#CATEGORIES OF THE CORPUS
categories()

#CATEGORIES OF CORPUS CORRESPONDING TO THESE FILES
categories([fileids])

#RAW CONTENT OF CORPUS
raw()

#RAW CONTENT OF SPECIFIED FILES
raw(fileids=[f1, f2, f3])

#RAW CONTENT OF SPECIFIED CATEGORIES
raw(categories=[c1, c2])

#WORDS OF THE WHOLE CORPUS
words()

#WORDS OF SPECIFIED FILEIDS
words(fileids=[f1, f2, f3])

#WORDS OF SPECIFIED CATEGORIES
words(categories=[c1, c2])

#SENTENCES OF SPECIFIED CATEGORIES
sents()

#SENTENCES OF SPECIFIED FILEIDS
sents(fileids=[f1, f2, f3])

#SENTENCES OF SPECIFIED CATEGORIES
sents(categories=[c1, c2])

#LOCATION OF GIVEN FILE ON DISK
abspath(fileid)

#ENCODING OF THE FILE (IF KNOWN)
encoding(fileid)

#OPEN STREAM FOR READING GIVEN CORPUS FILE
open(fileid)

#PATH TO THE ROOT OF LOCALLY INSTALLED CORPUS
root()

#CONTENTS OF README FILE OF THE CORPUS
readme()