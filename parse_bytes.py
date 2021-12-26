# parse_bytes

import re

def parse_bytes(input):
    byte_regex = re.compile(r'\b[10]{8}\b')
    return byte_regex.findall(input)
  
 

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is 10101010 11100010"))
print(parse_bytes("asdsa"))



