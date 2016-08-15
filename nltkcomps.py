from nltk.book import *

print len(text1)

print len(set(text1))

#prints vocabulary count after removing uppercase characters
print len(set(word.lower() for word in text1))

#prints vocabulary count after removing uppercase chars and
#removing punctuation in text1
print len(set([word.lower() for word in text1 if word.isalpha()]))