# valid_time

import re

def is_valid_time(input):
    time_regex = re.compile(r'\d{1,2}:\d{2}')
    match = time_regex.fullmatch(input)
    if match:
        return True
    return False


print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:23"))