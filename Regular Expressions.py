# Regular Expressions are used to search for patterns in a string or text
# Raw strings are what regular expressions are and what they are used on
# print(r"Hello \n World")

# import the regular expression module
import re
string = "abc"
pattern = "a"
if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')
