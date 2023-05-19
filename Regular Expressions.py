# Regular Expressions are used to search for patterns in a string or text
# Raw strings are what regular expressions are and what they are used on
# print(r"Hello \n World")

# import the regular expression module
# Match
# import re
# string = "abc"
# pattern = "a"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No match found')

# Search
# import re
# string = "bca"
# pattern = "a"
# if re.search(pattern, string):
#     print('Match found')
# else:
#     print('No match found')

# Metacharacters in regular expressions
# They are a special set of characters which don't match themselves, instead, they create some pattern which should be matched.
# Examples: *, +, {...}, ., ?, ^
# * - makes sure that a particular character preceding it is present 0 or more times

# # Star Metacharacter
# import re
# string = "abbbc"
# pattern = "ab*c"  # checking for weather b is present 0 or more times
# if re.search(pattern, string):
#     print('Match found')
# else:
#     print('No match found')

# + - means that the character preceding it is present at least one times
# Plus Metacharacter

# import re
# string = "abc"
# pattern = r"ab+c"  # checking for weather b is present at least one times
# if re.search(pattern, string):
#     print('Match found')
# else:
#     print('No match found')

# {} - means that the character preceding it is repeated the number of times that is stated inside the braces
# Curly braces Metacharacter

# import re
# string = "abb"
# pattern = r"ab{2}"  # checking for weather b is present at least 2 times
# if re.search(pattern, string):
#     print('Match found')
# else:
#     print('No match found')

# . - means that the symbol can take place of any other symbol
# Wildcard Metacharacter

# import re
# string = "adb"
# pattern = r"a.b"  # checking for weather a and b start and end respectively
# if re.search(pattern, string):
#     print('Match found')
# else:
#     print('No match found')


# ? - means that the character preceding it is optional, ie it may or may not be present
# Wildcard Metacharacter

# import re
# string = "pythonfile"
# pattern = r"python-?file"  # checking for weather character is present or not
# if re.search(pattern, string):
#     print('Match found')
# else:
#     print('No match found')


# ^ - means that the match must start at the beginning of the line or string
# Caret Metacharacter

import re
string = "91878889878"
pattern = r"^91"  # checking for weather string starts with 91
if re.search(pattern, string):
    print('Match found')
else:
    print('No match found')