# display_names

def display_names(first, second):
    return f"{first} say hello to {second}"

names = {"first": "Colt", "second": "Rusty"}

print(display_names(**names))

print(display_names(first="Charlie", second="Sue"))
