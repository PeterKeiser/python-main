# phone

import re

# def extract_phone(input):
#     phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
#     match = phone_regex.search(input)
#     if match:
#         return match.group()
#     return None

# print(extract_phone("my number si 345 468-6387"))
# print(extract_phone("my number si 345 468-638722"))
# print(extract_phone("345 468-6387 is my number"))
# print(extract_phone("345 468-6387"))


# def extract_all_phones(input)
#     phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
#     return phone_regex.findall(input)
    
# print(extract_all_phones("my number si 345 468-6387 or 396 476-2945"))
# print(extract_all_phones("my number si 345 468-63"))



# def is_valind_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False    

def is_valind_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False 

print(is_valind_phone("345 468-6387"))
print(is_valind_phone("345 468-6387 dfr"))
print(is_valind_phone("vftg 345 468-6387 d"))


