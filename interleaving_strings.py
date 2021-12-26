# interleaving_strings

# def interleave(strg1, strg2):
#         return zip(strg1, strg2)

# print(list(interleave("hello", "world")))

def interleave(strg1, strg2):
        return "".join("".join(x) for x in (zip(strg1, strg2)))

print(interleave("hello", "world"))





