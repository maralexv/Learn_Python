"""
Regular expressions are text-matching patterns described with a
formal syntax. You'll often hear regular expressions referred
to as 'regex' or 'regexp' in conversation. Regular expressions
can include a variety of rules, from finding repetition, to
text-matching, and much more.

One of the most common uses for the re module is for finding
patterns in text. Let's do a quick example of using the search
method in the re module to find some text...
"""

import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' % (pattern, text))

    # Check for match
    if re.search(pattern, text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

