import re
import nltk
from nltk.corpus import treebank
from nltk import FreqDist
word = 'supercalifragilisticexpialidocious'
# Finds all vowels in word
print(re.findall(r'[aeiou]', word))
# Finds number of vowels in word
print(len(re.findall(r'[aeiou]', word)))

print("----------------------------------------------------------------------")
# Prints 12 most common sequences of > 2 vowels
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj
for vs in re.findall(r'[aeiou]{2,}', word))
print(fd.most_common(12))
