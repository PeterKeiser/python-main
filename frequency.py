# frequency

def frequency(collection, v):
    return collection.count(v)

print(frequency([1, 2, 3, 4, 5, 3, 2, 4, 1, 1, 1,], 1))
print(frequency([1, 2, 3, 4, 5, 3, 2, 4, 1, 1, 1,], 3))
print(frequency([True, True, False, True, False, True, False], True))
