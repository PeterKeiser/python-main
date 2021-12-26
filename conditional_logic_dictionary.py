# conditional_logic_dictionary

num_list = [1, 2, 3, 4]
print(num_list)

# results = {num:("even" if num % 2 == 0 else "odd") for num in num_list} 
# print(results)

results = {num:("even" if num % 2 == 0 else "odd") for num in range(1,101)} 
print(results)