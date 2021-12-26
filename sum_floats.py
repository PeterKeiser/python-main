# sum_floats

def sum_floats(values):
    return sum(value for value in values if type(value) == float)

print(sum_floats([1, 2.3, 3, 4.654, 5, 6.982231]))
print(sum_floats([]))
    

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

print(sum_floats(1, 2.3, 3, 4.654, 5, 6.982231))
print(sum_floats())





