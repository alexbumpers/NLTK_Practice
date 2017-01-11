import nltk
import re

raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'..."""

print(re.split(r' ', raw))
print("-------------------------")
print(re.split(r'[ \t\n]+', raw))
print("-------------------------")
print(re.split(r'\W+', raw))
print("-------------------------")
print(re.findall(r'\w+|\S\w*', raw))
print("-------------------------")
print(re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw))


"""
Word    Function

\b	Word boundary (zero width)
\d	Any decimal digit (equivalent to [0-9])
\D	Any non-digit character (equivalent to [^0-9])
\s	Any whitespace character (equivalent to [ \t\n\r\f\v])
\S	Any non-whitespace character (equivalent to [^ \t\n\r\f\v])
\w	Any alphanumeric character (equivalent to [a-zA-Z0-9_])
\W	Any non-alphanumeric character (equivalent to [^a-zA-Z0-9_])
\t	The tab character
\n	The newline character
"""
