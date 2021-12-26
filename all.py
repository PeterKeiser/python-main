# all

all ([0, 1, 2, 3])

all([char for char in "eio" if char in "aeiou"])

characters = ["a", "b", "c", "e", "i"]
([char for char in "eio" if char in "aeiou"])

[num for num in [4, 2, 10, 6, 8] if num % 2 == 0]
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])

people = ["Charlie", "Casy", "Cody", "Carly", "Cristina"]

all([name[0]=="C" for name in people])


nums = [2, 60, 26, 18, 21]
all([num % 2 == 0 for num in nums])

nums = [2, 60, 26, 18, 21]
any([num % 2 != 0 for num in nums])

any([val for val in [1,2,3] if val > 2])
all([val for val in [1,2,3] if val > 5])

any([0, 1, 2, 3])
all([0, 1, 2, 3])

nums = [2, 60, 26, 18, 21]
any([num % 2 == 0 for num in nums])

nums = [2, 60, 26, 18, 21]
all([num % 2 == 0 for num in nums])


