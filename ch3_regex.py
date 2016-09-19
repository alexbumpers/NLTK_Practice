import re
import nltk
from nltk.corpus import words
from nltk.corpus import nps_chat
from nltk.corpus import treebank

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
# re.search searches for words ending with the string 'ed' in w
print([w for w in wordlist if re.search('ed$', w)])
print('-----------------------------------------------------------')
# The . wildcard symbol matches any single character.
# Suppose we have room in a crossword puzzle for an 8-letter word with j as its
# third letter and t as its sixth letter. In place of each blank cell we use a
# period:
print([w for w in wordlist if re.search('..j..t..$', w)])
# Adversely, '^' as opposed to '$' matches the start of a string:
print([w for w in wordlist if re.search('^..j..t..', w)])
print('-----------------------------------------------------------')
# The '?' specifies that the previous character is optional:
# print(sum(1 for w in text if re.search('^e-?mail$', w)))

# The T9 system is used for entering text on mobile phones. Two or
# more words that are entered with the same sequence of keystrokes are known as
# textonyms. E.g., both hole and golf are entered by pressing the sequence
# 4653. Here we use the regular expression «^[ghi][mno][jlk][def]$»:
print([w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)])
print("-------------------------------------------------------------------")

chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
print([w for w in chat_words if re.search('^l+o+l+$', w)])
print([w for w in chat_words if re.search('^[ha]+$', w)])
print([w for w in chat_words if re.search('^m*i*n*e*$', w)])

# The ^ operator has another function when it appears as the first character
# inside square brackets. E.g., «[^aeiouAEIOU]» matches any character other
# than a vowel. We can search the NPS Chat Corpus for words that are made up
# entirely of non-vowel characters using «^[^aeiouAEIOU]+$» to find items
# like these: :):):), grrr, cyb3r and zzzzzzzz. Notice this includes
# non-alphabetic characters.

# Examples of regex used to find particular patterns
wsj = sorted(set(nltk.corpus.treebank.words()))
# Searches for float numbers
print([w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)])
# Prints A-Z phrases ending in $
print([w for w in wsj if re.search('^[A-Z]+\$$', w)])
# Prints four character numbers (e.g., 2000)
print([w for w in wsj if re.search('^[0-9]{4}$', w)])
# Prints phrases like "10-word" if 'word' is between 3 and 5 characters
print([w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)])
# Prints phrases like word-and-otherword where each word has fewer than 6 chars
print([w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)])
# Prints words ending in 'ed' or 'ing'
print([[w for w in wsj if re.search('(ed|ing)$', w)]])
