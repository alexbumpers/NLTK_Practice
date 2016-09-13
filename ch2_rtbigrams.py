import nltk

#sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and',
            #'the', 'earth', '.']

##creates list of bigrams from var sent
#nltk.bigrams(sent)

##
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

print "--- ConditionalFreqDist of most common bigrams in Genesis ---"
print cfd['Earth']

print "--- Generates random text from bigram data above ---"
print generate_model(cfd, 'Earth')
