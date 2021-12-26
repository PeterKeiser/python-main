# basic regex

# import regex module

import re

# define our phone numer regex
# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# pattern = re.search(r'\d{3} \d{3}-\d{4}',"Call me at 415 555-4242").group()
pattern = re.findall(r'\d{3} \d{3}-\d{4}',"Call me at 415 555-4242 or 345 987-0987!")

# serch a string with our regex


# res = pattern.search('Call me at 415 555-4242 or 345 987-0987!')
# res = pattern.findall('Call me at 415 555-4242 or 345 987-0987!')
# print(type(pattern))
# print(res)
print(pattern)
# print(res.group())


