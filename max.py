# max

# print(max(3, 67, 99 ))

# print(max("c", "d", "a"))

# print(max([3, 4, 1, 2]))

# print(max((1, 2, 3, 4)))

# print(max("awesome"))

# print(max({1: "a", 3: "c", 2: "b"}))

# nums = (40, 32, 6, 5, 10)
# print(max(nums))

# print(min(nums))

# print(max("hello world"))
# print(min("hello world"))

# print(max(3, 5, 23, 65))

names = ["Arya", "Samson", "Dora", "Tim","Ollivander"]


# print(min(names))
# print(max(names))

# print(min(len(name) for name in names))

# print(max(names, key=lambda n: len(n)))

# print(min(names, key=lambda n: len(n)))


songs = [
    {"tittle": "happy birthday", "playcount" : 1},
    {"tittle": "Survive", "playcount": 6},
    {"tittle": "YMCA", "playcount": 99},
    {"tittle": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda s: s["playcount"]))
print(max(songs, key=lambda s: s["playcount"]))
print(max(songs, key=lambda s: s["playcount"])["tittle"])

max=0
for song in songs:
    if song["playcount"]>max:
        max = song["playcount"]
print(max)



