# first_generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
    




# c =count_up_to(10)
# for num in c:
#     print(num)

# print(next(c))
# print(next(c))
# print(next(c))

c = count_up_to(10)
print(next(c))

for num in c:
    print(num)

# help(c)


