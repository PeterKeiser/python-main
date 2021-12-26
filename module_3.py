# module_3

# import keyword

# def contains_keyword(strigs):
#     if(keyword.iskeyword(n) for n in strigs):
#         return True
#     else:
#         return False
    
# print (contains_keyword(["hello", "peter", "goal"]))
# print (contains_keyword(["hello", "peter", "house"]))
# print (contains_keyword(["hello", "goodbye"]))
# print (contains_keyword(["def", "for", "def"]))


import keyword

def contains_keyword(*args):
    for n in args:
        if keyword.iskeyword(n):
            return True
    else:
        return False
    
print (contains_keyword("hello", "peter", "goal"))
print (contains_keyword("hello", "peter", "house"))
print (contains_keyword("hello", "goodbye"))
print (contains_keyword("def", "for", "def"))



