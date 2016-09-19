# Wildcard, matches any character
.
# Matches some pattern abc at the start of a string
^abc
# Matches some pattern abc at the end of a string
abc$
# Matches one of a set of characters
[abc]
# Matches one of a range of characters
[A-Z0-9]
# Matches one of the specified strings (disjunction)
ed|ing|s
# Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure)
*
# One or more of previous item, e.g. a+, [a-z]+
+
# Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]?
?
# Exactly n repeats where n is a non-negative integer
{n}
# At least n repeats
{n,}
# No more than n repeats
{,n}
# At least m and no more than n repeats
{m,n}
# Parentheses that indicate the scope of the operators
a(b|c)+
