import nltk

## Exercise 1
#phrase = ['Computer', 'Python', 'Language', 'C++', 'Programming']


#def phrase_add():
    #ps = phrase[1] + " " + raw_input()
    #return ps

#print phrase_add()
#x = phrase_add()

## Exercise 2
#from nltk.corpus import gutenberg
#print gutenberg.fileids()

##for fileid in gutenberg.fileids():
#len_austen = len(gutenberg.words('austen-persuasion.txt'))
#print len_austen

## Exercise 3

#from nltk.corpus import brown

#print brown.words(categories='fiction')
#print brown.words(categories='humor')

## Exercise 4

#from nltk.corpus import state_union

#cfd_sotu = nltk.ConditionalFreqDist((target, fileid)
#for fileid in state_union.fileids()
#for w in state_union.words(fileid)
#for target in ['men', 'women', 'people']
#if w.lower().startswith(target))
#print cfd_sotu.plot()

## Exercise 5
##3 types of meronyms and holonyms --> member_, part_, substance_
#from nltk.corpus import wordnet as wn

#pm_car = wn.synset('car.n.01').part_meronyms()
#print pm_car
#mm_car = wn.synset('car.n.01').member_meronyms()
#print mm_car
#sm_car = wn.synset('car.n.01').substance_meronyms()

#ph_fight = wn.synset('fight.n.01').part_holonyms()
#print ph_fight
#mh_fight = wn.synset('fight.n.01').member_holonyms()
#print mh_fight
#sh_fight = wn.synset('fight.n.01').substance_holonyms()
#print sh_fight

## Exercise 6
# Problem: meanings change as you translate and retranslate, making the
# translations inaccurate.

## Exercise 7

#from nltk.book import *
#print text1.concordance('however')

#from nltk.corpus import gutenberg
#print gutenberg.fileids()
#austen_however_text = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#print austen_however_text.concordance("however")

## Exercise 8
## def a cond freq dist over names corpus that allows us to see which initial
## letters are more frequent for males vs females

#from nltk.corpus import names

#names = nltk.corpus.names
#print names.fileids()
#male_names = names.words('male.txt')
#female_names = names.words('female.txt')

#cfd_firstletters = nltk.ConditionalFreqDist((fileid, name[1])
#for fileid in names.fileids()
#for name in names.words(fileid))
#print cfd_firstletters.plot()
##most names start with the letter 'a'

## Exercise 9
## Pick 2 texts, study differences b/w them in terms of vocab, vocab richness,
## genre, etc. Find a pair of words with very different meanings b/w texts.
#import nltk.corpus
#from nltk.corpus import brown
#from nltk.text import Text

#print brown.categories()

#print ">ADVENTURE< VOCAB FROM >BROWN<"
#sorted(set(brown.words(fileids=['cn15'])))
#print ">ROMANCE< VOCAB FROM >BROWN<"
#sorted(set(brown.words(fileids=['cp12'])))

#ADV_TEXT = Text(nltk.corpus.brown.words(fileids=['cn15']))
#ROM_TEXT = Text(nltk.corpus.brown.words(fileids=['cp12']))

#def TEXT_CONCORDANCE():
    #ADV_CONC = ADV_TEXT.concordance("scare")
    #print ">ADVENTURE< VOCAB FROM >BROWN<"
    #print ADV_CONC

    #print ">ROMANCE< VOCAB FROM >BROWN<"
    #ROM_CONC = ROM_TEXT.concordance("scare")
    #print ROM_CONC


#print TEXT_CONCORDANCE()

#from nltk.book import text6, text7
## Exercise 10
## How many word types account for 1/3 of word tokens for a variety of texts?

#tokens_text6 = str(len(text6))
#print "Number of tokens in text6: " + tokens_text6

#tokens_text7 = str(len(text7))
#print "Number of tokens in text7: " + tokens_text7

#wordtypes_text6 = str(len(set(text6)))
#print "Number of word types in text6: " + wordtypes_text6

#wordtypes_text7 = str(len(set(text7)))
#print "Number of word types in text7: " + wordtypes_text7

#text6_ = nltk.book.text6

#cfd = nltk.ConditionalFreqDist((text6, "the")
#for text6 in text6_)

#print cfd.plot()

#from nltk.corpus import brown

#cfd = nltk.ConditionalFreqDist((genre, word)
#for genre in brown.categories()
#for word in brown.words(categories=genre))

#genres = ['religion', 'science_fiction', 'adventure']

## Exercise 12
## How many distinct words does CMU PronDict contain? What fraction of words in
## this dictionary have more than one pronunciation?

#from nltk.corpus import cmudict
#pron = cmudict.dict()

#multi_pronunciation_word_ct = 0
#word_ct = 0

#for word in pron:
   #word_ct += 1
   ## if a word appears in cmudict.dict() more than once, add that number
   ## to multi_pronunciation_word_ct
   #if len(pron[word]) > 1:
    #  multi_pronunciation_word_ct += 1
## %x.yf%% species (x) radix point number and (y) how many places from
## .0 will be shown. i.e., 0.00000 when y = .5; 'f' specifies float as type.
#print ('%2.5f%% of the %d words in the dictionary have multiple pronunciations'
 #% ((float(multi_pronunciation_word_ct)*100)/word_ct,word_ct))

## Exercise 13
## What percentage of noun sets have no hyponyms?
## Doesn't work...
#from nltk.corpus import wordnet as wn
#noun_synsets = list(wn.all_synsets('n'))
#print noun_synsets
#types_of_nouns = noun_synsets.hyponyms()
#print types_of_nouns[25]


## Exercise 14
## Come back to this later.
#from nltk.corpus import wordnet as wn
#def supergloss(s):
    #print "SYNSET DEFINITIONS"
    #for synset in wn.synsets(s, wn.NOUN):
        #types_of_s = synset.hyponyms()
        #print (str(synset.name()) + ':', str(synset.definition()) +
        #" -- HYPONYMS: ", str(types_of_s))
    #print s
    #return;

#print supergloss('mint')

## Exercise 15
## All words that occur >= 3 times in brown corpus
## Come back to this later.
#from nltk.corpus import brown
#from nltk import FreqDist

#def many_words(corpus, number):
    #fdist = nltk.FreqDist([w.lower() for w in corpus])
    #words = [' ']
    #for word in fdist:
    #    if fdist[word] >= len(str(number)):
            #words.append(word)
    #return words
#print many_words('nltk.corpus.brown.words', 3)

## Exercise 16
## Write a program to generate a table of lex diversity scores (i.e.,
## token/type generators, like in table 1.1. Include full set of Brown Corpus
## genres. Which has the lowest diversity? Is this expected?)
## Prints correct values, but not in table format.

#from nltk.corpus import brown
#def brown_table():
    #brown_cats = nltk.corpus.brown.categories()

    #for genre in brown_cats:
        #tokens = len(nltk.corpus.brown.words(categories=genre))
        #vocab = len(set(nltk.corpus.brown.words(categories=genre)))
        #diversity = tokens / vocab
        #print genre, tokens, vocab, diversity
    #return;

#print brown_table()

## Exercise 17

## Defines function to find 50 most frequently occuring words that are not
## stopwords.
import nltk.corpus
from nltk.book import *
from nltk import FreqDist


#def FDIST_NONSTOPS(text):
    #stopwords = nltk.corpus.stopwords.words('english')
    #nonstops50_fdist = FreqDist([w for w in text if w not in stopwords])
    #return nonstops50_fdist.items()[:50]
#stopwords = nltk.corpus.stopwords.words('english')
#content = [w for w in text if w.lower() not in stopwords]
#return float(len(content)) / float(len(text))
    #nonstops50_cfdist = nonstops50_fdist.plot(50, cumulative=True)
    #print nonstops50_cfdist
    #return nonstops50_cfdist;
#print FDIST_NONSTOPS(text1)

#def PLOT_NONSTOPS():
    #nonstop_plot = FreqDist(text1).plot(50, cumulative=True)
    #return nonstop_plot

#PLOT_NONSTOPS()

#def content_fraction(text):
    #stopwords = nltk.corpus.stopwords.words('english')
    #content = [w for w in text if w.lower() not in stopwords]
    #return float(len(content)) / float(len(text))

#print content_fraction(text1)

## Exercise 18
## Write a program to print 50 most frequent bigrams, omitting bigrams that
## contain stopwords.
from nltk.util import bigrams

def FIFTY_BIGRAMS(text):
    bigrams = nltk.bigrams(text)
    stopwords = nltk.corpus.stopwords.words('english')
    bigrams50_fdist = FreqDist([w for w in bigrams if w[1] not in stopwords])
    return bigrams50_fdist.items()[:50]

print FIFTY_BIGRAMS(text1)

## Exercise 19
## Write a program to create a table of word frequencies by genre, like the one
## given in section 2.1 for modals. Choose your own words and try to find words
## whose presence (or absenece) is typical of a genre. Discuss findings.
