# Translation to unicode is called 'decoding'. Conversely, writing out
# Unicode to a file or terminal, we translate it into a suitable encoding
# and this is called 'encoding'

import nltk
# io and shutil imported to allow for .encode() module in Python 2.7
#import io
#import shutil
# Lets us inspect properties of Unicode characters
import unicodedata
import re

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
# Doc string below is python 2.7
"""f = io.open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))

nacute = '\u0144'
print nacute
print nacute.encode('utf8')

lines = io.open(path, encoding='latin2').readlines()
line = lines[2]
print line.encode('unicode_escape')
for c in line:
        if ord(c) > 127:
            print '{} U+{:04x} {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c))"""

f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))

print(ord('ń'))
nacute = '\u0144'
print(nacute)
print(nacute.encode('utf8'))

# Prints UTF-8 byte sequence, followed by code point integer using standard
# Unicode convention (i.e., prefix hex digits with u+) followed by their
# unicode name
lines = open(path, encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
for c in line:
    if ord(c) > 127:
        print('{} U+{:04x} {}'.format(c, ord(c), unicodedata.name(c)))

# Illustrates how Python str methods and re module work w/ Unicode characters
print(line.find('zosta\u0142y'))
line = line.lower()
print(line)
print(line.encode('unicode_escape'))
# \w matches a 'word character'
m = re.search('\u015b\w*', line)
# See https://docs.python.org/2/library/re.html for more info on .group
print(m.group())
print(word_tokenize(line))
