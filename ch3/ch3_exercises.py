import nltk

""" Exercise 1 """
s = 'colorless'
print(s[0:4]+"u"+s[4:])

""" Exercise 2 """
morph_list = ['dishes', 'running', 'nationality', 'undo', 'preheat']
for x in morph_list:
    if x[4:] == 'es':
        print(x[:-2])
    if x[3:] == 'ning':
        print(x[:-4])
    if x[6:] == 'ality':
        print(x[:-5])
    if x[2:] == 'do':
        print(x[:-2])
    if x[3:] == 'heat':
        print(x[:-4])

""" Exercise 3 """
for x in morph_list:  # What happens if we go to the left of a string?
    (x[:-30])

""" Exercise 4 """
for x in morph_list:
    print(x[1::2])
    print(x[1::-2])
    print(x[::-1])

""" Exercise 6 """
# [a-zA-Z]+  # Matches all instances of chars a-z and A-Z
# [A-Z][a-z]*  # Matches all instances of A-z (e.g., Text, but not text)
# p[aeiou]{,2}t  # Matches words starting with p, at least 2 vowels in between, ending in t. E.g., 'pot' or 'poot'
# \d+(\.\d+)?  # Matches all float and int numbers ()
# ([^aeiou][aeiou][^aeiou])*  # Matches vowel+consonant? (e.g., "er")
# \w+|[^\w\s]+  # Matches all whitespace, chars, numbers, etc.

""" Exercise 7 """
# '^(a|an|the)$'  #  Matches single instance of a/an/the
# [0-9+*0-9+*0-9]  #  Matches mathematical expressions a+b*c or a*b+c, etc.

""" Exercise 8 """
from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize

def html_strip(url):
    site_to_strip = request.urlopen(url).read().decode('utf-8')
    no_html = BeautifulSoup(site_to_strip).get_text()
    tokenized_site = word_tokenize(no_html)
    print(tokenized_site)
html_strip('http://nltk.org/')
