import nltk
from nltk.corpus import gutenberg
#gutenberg.fileids()

#def unusual_words(text):
    #text_vocab = set(w.lower() for w in text if w.isalpha())
    #english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    ## .difference() returns new set with elements in x but not y
    ## in this example, text_vocab = x ; english_vocab = y
    #unusual = text_vocab.difference(english_vocab)
    #return sorted(unusual)

#print unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))

#print unusual_words(nltk.corpus.nps_chat.words())


## -------- stopwords --------
## stopwords are high frequency words like the, to, and, also, etc.

#from nltk.corpus import stopwords
#from nltk.corpus import gutenberg
#gutenberg.fileids()

#print stopwords.words('english')
##just returns 0 for some reason
#def content_fraction(text):
    #stopwords = nltk.corpus.stopwords.words('english')
    #content = [w for w in text if w.lower() not in stopwords]
    #return len(content) / len(text)

#print content_fraction(nltk.corpus.gutenberg.words('austen-sense.txt'))

##same as line 26
#def content_fraction(text):
    #stopwords = nltk.corpus.stopwords.words('english')
    #content = [w for w in text if w.lower() not in stopwords]
    #return len(content) / len(text)

#print int(content_fraction(nltk.corpus.reuters.words()))

## -------- SEE 2-6 ON PAGE 61 -------
##letters in the puzzle. They must all be used once per word.
##each word must contain 'r' and there must be at least one 9 letter word
##no plurals ending in 's', no foreign words, no proper names.
#puzzle_letters = nltk.FreqDist('egivrvonl')
#obligatory = 'r'
#wordlist = nltk.corpus.words.words()
#puzzle_solution = [w for w in wordlist if len(w) >= 4
                    #and obligatory in w
                    #and nltk.FreqDist(w) <= puzzle_letters]
#print puzzle_solution

# ----- names by gender -----

#import nltk
#from nltk.corpus import names

#print names.fileids()
#male_names = names.words('male.txt')
#female_names = names.words('female.txt')
#print [w for w in male_names if w in female_names]


##returns last letter of names by sex in c_freqdist, then plots it
#cfd = nltk.ConditionalFreqDist(
        #(fileid, name[-1])
        #for fileid in names.fileids()
        #for name in names.words(fileid)
#)
#print cfd.plot()

## ----- CMU Pronouncing Dictionary -----
import nltk
from nltk.corpus import cmudict

entries = nltk.corpus.cmudict.entries()
print len(entries)

for entry in entries[39943:39951]:
    print entry

##scans lexicon looking for entires who pronunciation consists of 3 phones
##if true, assigns contents of pron to 3 variables: ph1, ph2, ph3
for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print word, ph2
##for loop that returns/prints all words ending with -nicks pronunciation
syllable = ['N', 'IH0', 'K', 'S']
print [word for word, pron in entries if pron[-4:] == syllable]

## For loop that returns words ending with 'mn' pronunciation, where 'M'
## is pronounced with a silent n
print [w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']

## Print beginning of words where 'N' is pronounced and the letter preceding
## it is silent (e.g.: knob, pneumonia, knife)
print sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and
        w[0] != 'n'))

## Phones contain digits to represent primary stress (1), secondary stress (2),
## no stress (0).
## Function below defines function to extract stress digits and then scan
## lexicon to find words w/ particular stress pattern.

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]
print [w for w, pron in entries if stress(pron) == ['0', '1', '2', '0']]
print [w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]

## Finds all 'p' word consisting of three sounds, groups them according to
## their first and last sounds.

##p words with 3 sounds
p3 = [(pron[0] + '-' + pron[2], word)
        for (word, pron) in entries
        if pron[0] == 'P' and len(pron) == 3]

## ConditionalFreqDist of p3
cfd = nltk.ConditionalFreqDist(p3)

##
for template in cfd.conditions():
    if len(cfd[template]) > 10:
        words = cfd[template].keys()
        wordlist = ' '.join(words)
        print template, wordlist[:70] + "..."

prondict = nltk.corpus.cmudict.dict()
print prondict['fire']
##'blog' doesn't exist in cmudict.dict(), gives KeyError
#print prondict['blog']
##assigns pron to 'blog' in this script
prondict['blog'] = ['B', 'L', 'AA1', 'G']
print prondict['blog']

text = ['natural', 'language', 'processing']
print [ph for w in text for ph in prondict[w][0]]
