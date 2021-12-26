# filter

nums = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 != 0, nums))

print(evens)



names = ["austin", "penny", "anthony", "angel", "billy"]

newlist = list(filter(lambda name: name[0] == "a", names))

print(newlist)