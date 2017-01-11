#from nltk.corpus import webtext


#for fileid in webtext.fileids():
    #print fileid, webtext.raw(fileid)[65:85]
    
##date, chatroom, number of posts. From naval postgrad school
#from nltk.corpus import nps_chat
#chatroom = nps_chat.posts('10-19-20s_706posts.xml')
#print chatroom[19]

#from nltk.corpus import brown
#prints categories/genres in Brown Corpus
#print brown.categories()
#prints words in the 'news' category
#print brown.words(categories='news')
#prints words in 'cg22'
#print brown.words(fileids=['cg22'])
#prints sentences in news > editorials > reviews
#print brown.sents(categories=['news', 'editorial', 'reviews'])

#from nltk.corpus import gutenberg

#gutenberg.fileids()

##sentence in Macbeth
#macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
#print macbeth_sentences

#import nltk
#from nltk.corpus import brown
#from nltk import FreqDist

#hobbies_text = brown.words(categories='hobbies')
##freqdist of lowercase modals in 'hobbies'
#fdist = nltk.FreqDist([w.lower() for w in hobbies_text])
##modal has to do with ability and neccessity
#modals = ['can', 'could', 'may', 'might', 'must', 'will']

##for-loop that prints a string + modals + fdist of m
#for m in modals:
    #print 'These are the modals in hobbies ' + m + ':', fdist[m]
    
##prints table of genres(conditions) and modals(samples)
#cfd = nltk.ConditionalFreqDist(
            #(genre, word)
            #for genre in brown.categories()
            #for word in brown.words(categories=genre))
#genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
#modals = ['can', 'could', 'may', 'might', 'must', 'will']
#print cfd.tabulate(conditions=genres, samples=modals)

##----------------------##
##REUTERS CORPUS
#from nltk.corpus import reuters
#print reuters.fileids()
##print reuters.categories()
#print reuters.categories('training/9865')
#print reuters.categories(['training/9865', 'training/9880'])
#print reuters.fileids('barley')
#print reuters.fileids(['barley', 'corn'])

#print reuters.words('training/9865')[:14]
#print reuters.words(['training/9865', 'training/9880'])
#print reuters.words(categories='barley')
#print reuters.words(categories=['barley', 'corn'])

##-----------------------##
##INAUGURAL CORPUS
#import nltk
#from nltk.corpus import inaugural
#from nltk import FreqDist

#print inaugural.fileids()
## [:4] is used because it prints the first 4 chars (the year in this case)
#print [fileid[:4] for fileid in inaugural.fileids()]

##---------CONDITIONAL FREQUENCY DISTRIBUTION OF INAUGURAL-----------

#cfd = nltk.ConditionalFreqDist(
            #(target, fileid[:4])
            #for fileid in inaugural.fileids()
            #for w in inaugural.words(fileid)
            #for target in ['america', 'citizen']
            #if w.lower().startswith(target))
##plots conditional freq dist for 'america' and 'citizen' in inaugurals
#cfd.plot()

##
import nltk
print nltk.corpus.cess_esp.words()
print nltk.corpus.floresta.words()
print nltk.corpus.indian.words()
##UDHR is the Univeral Declaration of Human Rights
print nltk.corpus.udhr.fileids()
print nltk.corpus.udhr.words('Javanese-Latin1')[11:]

from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut',
             'Hungarian_Magyar', 'Ibibio_Efik']
#cfd = nltk.ConditionalFreqDist(
            #(lang, len(word))
            #for lang in languages
            #for word in udhr.words(lang + '-Latin1'))
#cfd.plot(cumulative=True)
print nltk.corpus.udhr.fileids()
#plots freqdist of words in Amahuaca language
raw_text = udhr.raw('Amahuaca')
nltk.FreqDist(raw_text).plot()