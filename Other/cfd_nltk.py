#import nltk
#from nltk.corpus import brown
#cfd = nltk.ConditionalFreqDist(
            #(genre, word) ##ConditionalFreqDist(condition, event)
            #for genre in brown.categories()
            #for word in brown.words(categories=genre)
#)

#genre_word = [(genre, word) #for each word, loop over every word of genre
            #for genre in ['news', 'romance']
            #for word in brown.words(categories=genre)]
#print len(genre_word)
#print genre_word[:4]
#print genre_word[-4:]

#cfd = nltk.ConditionalFreqDist(genre_word)
#print cfd
#print cfd.conditions() #prints conditions in cfd

#print cfd['news'] #no. of tokens in news
#print cfd['romance'] #no. of tokens in romance
#print list(cfd['romance']) #list of tokens in romance
#print cfd['romance']['could'] #FD of occurrences of 'could' in 'romance'

## Inaugural cfd
#import nltk
#from nltk.corpus import inaugural
#cfd = nltk.ConditionalFreqDist(
            #(target, fileid[:4])
            #for fileid in inaugural.fileids()
            #for w in inaugural.words(fileid)
            #for target in ['america', 'citizen']
            #if w.lower().startswith(target)
#)
#print cfd

##Condition = name of language, counts plotted are from word lengths
#from nltk.corpus import udhr
#languages = ['Chickasaw', 'English', 'German_Deutsch',
            #'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
#cfd = nltk.ConditionalFreqDist(
            #(lang, len(word))
            #for lang in languages
            #for word in udhr.words(lang + '-Latin1')
#)
##1638 English words have 9 or fewer letters, etc.
#print cfd.tabulate(conditons=['English', 'German_Deutsch'],
            #samples=range(10), cumulative=True)

## Page 55 'your turn' exercise
## tabulate most newsworthy days of the week, most romantic days of week
import nltk
from nltk.draw.dispersion import dispersion_plot
from nltk.corpus import brown
from matplotlib.pyplot import *

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday']

genres = ['news', 'romance']

cfd = nltk.ConditionalFreqDist((genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)

)

print cfd.tabulate(conditions=genres, samples=days)

print cfd.plot(conditions=genres, samples=days)
