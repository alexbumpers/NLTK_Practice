import re
import nltk
from nltk.corpus import treebank
from nltk import FreqDist
from nltk import word_tokenize
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

print("----------------------------------------------------------------------")
# matches initial vowel sequences, final vowel sequences, and all consonants;
# everything else is ignored.
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

english_udhr = nltk.corpus.udhr.words('English-Latin1')
print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))

# Finds consonant-vowel pairs in Rotokas
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
print(cfd.tabulate())

# Finds list of words containing a given vowel pair
cv_word_pairs = [(cv, w) for w in rotokas_words
                for cv in re.findall(r'[ptksvr][aeiou]', w)]
# nltk.Index() indexes converts what would be, e.g., ('ka', 'kasuari') and so on, into a useful, easy to read index
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['su'])
print(cv_index['po'])

# Finding word stems
# Finds word stems by simply stripping anything that seems like a suffix
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
print([stem(t) for t in tokens])
