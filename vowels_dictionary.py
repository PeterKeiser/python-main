# vowels dictionary

# answer = {n:0 for n in ["a", "e", "i", "o", "u"]}
# print(answer)

# answer = {char:0 for char in "aeiou"}
# print(answer)

# answer = dict.fromkeys("aeiou", 0)
# print(answer)

answer = {num: chr(num) for num in range(65, 91)}
print(answer)

g = chr(66)
print(g)