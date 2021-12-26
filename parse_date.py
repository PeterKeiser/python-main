# parse_date

import re

def parse_date(input):
    date_regex = re.compile(r'(\d{2})(/|,|\.)(\d{2})(/|,|\.)(\d{4})')
    match = date_regex.fullmatch(input)
    if match:
        peter = {
            "d": match.group(1),
            "m": match.group(3),
            "y": match.group(5)
        }
        return peter
    return None


print(parse_date("01/12/1999"))
print(parse_date("12,04,2003"))
print(parse_date("12.11.2003"))


