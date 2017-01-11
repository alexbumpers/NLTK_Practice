import nltk

f = open('document.txt')
raw = f.read()
print raw

# Read file one line at a time
f = open('document.txt', 'rU')
for line in f:
    print line.strip()

# Accessing NLTK, etc.
path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
raw = open(path, 'rU').read()
print raw

# Use/import pypdf and pywin32 to access PDF and Word files
