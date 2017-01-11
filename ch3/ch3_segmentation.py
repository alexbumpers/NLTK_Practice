import nltk
from nltk.corpus import gutenberg
import pprint

text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = nltk.sent_tokenize(text)
pprint.pprint(sents[79:89])

print("-------------------------------------------------------------------")
text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
text2 = "thequickbrownfoxjumpedoverthelazydogs"
seg3 = "0010000100001001000001000100100010001"
seg4 = "0000100100000011001000000110000100010000001100010000001"

""" Function for segmenting texts using bits as a reference. Each '1'
should represent the end of a word or phrase. See printed methods for more
information."""
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):  # Iterate from 0 to the length (size) of segment
        if segs[i] == '1':  # If the index of segment is segs[1] ...
            words.append(text[last:i+1])  # Append via iteration last:i+1
            last = i+1  # Iterate last
    words.append(text[last:])  # Append text[last:] to words
    return words
print(segment(text, seg1))
print(segment(text, seg2))
print(segment(text2, seg3))
print("-------------------------------------------------------------------")

""" Calculation of Objective Function: Given a hypothetical segmentation of the
source text, derive a lexicon and a derivation table that permit
 the source text to be reconstructed, then total up the number of characters
used by each lexical item (including a boundary marker) and the number of
lexical items used by each derivation, to serve as a score of the quality of
the segmentation; smaller values of the score indicate a better segmentation.
See figure 3.8 in NLTK book for more info on this.
"""
def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = sum(len(word) + 1 for word in set(words))
    return text_size + lexicon_size

print(segment(text, seg4))
print("----------------------------------------------------------------")
""" Computing Cost of Storing Lexicon & Reconstructing the Source Text """
""" Search pattern of ones and zeros that minimizes the objective function.
Best segmentation includes 'words' like 'thekitty' since there's not enough
evidence in the data to split this further. """
from random import randint

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0, len(segs)-1))
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, round(temperature))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print()
    return segs

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
print(anneal(text, seg1, 5000, 1.2))
