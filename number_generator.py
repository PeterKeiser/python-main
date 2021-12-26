# number_generator

def nums():
    for num in range(1,10):
        yield num


# result= print(nums())
# print(next(result))

# g = nums()
# print(next(g))
# print(next(g))
# print(next(g))

# g2 = (num for num in range(1,10))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))

# l = [num for num in range(1,10)]
# print(l)

# print(sum([num for num in range(1,10)]))

import time
gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time 

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time 

print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")





