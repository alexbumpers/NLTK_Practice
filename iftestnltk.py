from nltk.book import *

word = 'cat'
if len(word) < 5:
    print 'word length is less than 5'

for word in ['Natural', 'Language', 'Toolkit', '.']:
    print word
    
sent1 = ['Natural', 'Language', 'Toolkit', 'software', '.']

for word in sent1:
    if word.endswith('t'):
        print word
        
for token in sent1:
    if token.islower():
        print token, 'is a lowercase word'
    elif token.istitle():
        print token, 'is a titlecase word'
    else:
        print token, 'is punctuation'
        
tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])

for word in tricky:
    print word,