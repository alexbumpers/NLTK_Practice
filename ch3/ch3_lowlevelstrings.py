# Basic string
monty = 'monty python'
print monty

# Multi-line string using triple quotes
couplet = """Rough winds do shake the darling buds of May,
And Summer's lease hath all too short a date:"""
print couplet

test = "Test"
print test + test + test
print test*3

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
    print(line)

# End=' ' only works in Python 3
#sent = 'colorless green ideas sleep furiously'
#sent = 'colorless green ideas sleep furiously'
#for char in sent:
#    print char, end=' '

from nltk.corpus import gutenberg
from nltk import FreqDist
import nltk
# Finds 5 most commonly occurring characters in Moby Dick
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print fdist.most_common(5)
# Descending list of most common characters in Moby Dick
print [char for (char, count) in fdist.most_common()]
fdist.plot()

# Accessing substrings
print "-------------------------"
# Finds string in string
phrase = "This is a test string used to find a certain word."
if 'none' in phrase:
    print 'found "none"'
else:
    print 'did not find word'

# Find position of substring in string
print monty.find('p')
