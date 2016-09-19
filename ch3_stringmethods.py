# index of first instance of string t inside s (-1 if not found)
s.find(t)
# index of last instance of string t inside s (-1 if not found)
s.rfind(t)
# like s.find(t) except it raises ValueError if not found
s.index(t)
# like s.rfind(t) except it raises ValueError if not found
s.rindex(t)
# combine the words of the text into a string using s as the glue
s.join(text)
# split s into a list wherever a t is found (whitespace by default)
s.split(t)
# split s into a list of strings, one per line
s.splitlines()
# a lowercased version of the string s
s.lower()
# an uppercased version of the string s
s.upper()
# a titlecased version of the string s
s.title()
# a copy of s without leading or trailing whitespace
s.strip()
# replace instances of t with u inside s
s.replace(t, u)
