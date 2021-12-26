# modules

import random as rand
from random import chice, randint

# rand.choice(["apple", "banana", "cherry", "durian"])
fruit = rand.choice(["apple", "banana", "cherry", "durian"])
print(rand.randint(1,100))
# rand.shuffle(["apple", "banana", "cherry", "durian"])
exotic_fruit = rand.shuffle(["apple", "banana", "cherry", "durian"])

print(fruit)
print(exotic_fruit)


from random import choice as pick, randint as magic_number_chooser, shuffle

fruit = pick(["apple", "banana", "cherry", "durian"])
print(magic_number_chooser(1,100))
exotic_fruit = ["apple", "banana", "cherry", "durian"]
print(exotic_fruit)
print(shuffle(["apple", "banana", "cherry", "durian"]))

print(fruit)
# print(exotic_fruit)






