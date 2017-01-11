import nltk
""" Exercise 9 """
""" Needs to be fixed later, hardcoding should be removed. Currently returns
empty list.
"""
""" def load():
    #open_file = open(f, 'r')
    f = "This is a text file used for example #9 in NLTK chapter-03."
    pattern = r'''(?x)          # set flag to allow verbose regexps
        (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
        \w+(?:-\w+)*        # words with optional internal hyphens
        \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
        \.\.\.              # ellipsis
        [][.,;"'?():_`-]    # these are separate tokens
    '''
    print(nltk.regexp_tokenize(f, pattern))
load()
"""

""" Exercise 10 """  # Rewrite as list comprehension
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = []
for word in sent:
    word_len = (word, len(word))
    result.append(word_len)
print(result)

test_comp = [(word, len(word)) for word in sent]  # List comp version of for loop above
print(test_comp)

""" Exercise 11 """
raw = 'The quick brown foxes jumped over the lazy dogs.'
print(raw.split('o'))

""" Exercise 12 """
oneperline = "Print out characters of this string: one per line!"

for char in oneperline:
    print(char)

""" Exercise 13 """
test_sent = "This is a test sentence for the split() function."
print(test_sent.split('\t'))

""" Exercise 14 """
words = ["goose", "beaver", "aardvark", "cat", "iguana", "dog", "frog", "horse", "elephant"]
print(sorted(words))
