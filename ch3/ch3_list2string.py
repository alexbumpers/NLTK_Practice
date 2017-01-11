import nltk

silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
print([' '.join(silly)])  # Joins all of the words in this last with a space b/w

fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in sorted(fdist):
    print(word, '->', fdist[word], end='; ')
print("\n")

for word in sorted(fdist):
    print('{}->{};'.format(word, fdist[word]), end=' ')  # String format example
print("\n")
print("---")
print('{}->{};'.format ('cat', 3))
print("\n")

template = 'Lee wants a {} right now'
menu = ['sandwich', 'spam fritter', 'pancake']
for snack in menu:
    print(template.format(snack))


def tabulate(cfdist, words, categories):
    print('{:16}'.format('Category'), end=' ')  # column headings
    for word in words:
        print('{:>6}'.format(word), end=' ')
    print()
    for category in categories:
        print('{:16}'.format(category), end=' ')  # row heading
        for word in words:  # for each word
            print('{:6}'.format(cfdist[category][word]), end=' ')  # print table cell
        print()  # end the row

from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
print(tabulate(cfd, modals, genres))
print("----")
