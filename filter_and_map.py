# filter_and_map

# names = ["Lassie", "Colt", "Rusty"]
# result = []
# result = (f"Your instructor is " + {*list(filter(lambda n: len(n) < 5, names))})

# print(result)

names = ["Lassie", "Colt", "Rusty"]
result = list(map(lambda name: f"Your instructor is {name}", filter(lambda n: len(n) < 5, names)))

print(result)

names = ["Lassie", "Colt", "Rusty"]
result2 = [f"Your instructor  is {name}." for name in names if len(name)<5]

print(result2)



