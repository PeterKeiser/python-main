# distionary_values

instructor = {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses" : 4,
    "favourite_language" : "Python",
    "is_hilarious" : True,
    44 : "my favourite number"
}

for value in instructor.values():
    print(value)

for k in instructor.keys():
    print(k)

for i in instructor.items():
    print(i)

for key, value in instructor.items():
    print(f"key is: {key} and value is: {value}")

