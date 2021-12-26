# map_in_action

names = [
    {"first":"Rusty", "last":"Steele"},
    {"first":"Colt", "last": "Steele"},
    {"first":"Blue", "last": "Steele"}
]

first_names = list(map(lambda x: x ["first"], names))
print(first_names)