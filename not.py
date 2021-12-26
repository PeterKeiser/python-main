# not

age = 1

# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dollars ticket for everyone else

if age <=1:
    print(f"You are infant of age:{age} and you can go for free.")
elif not ((age >= 2 and age <= 8) or age >= 65):
    print(f"You are {age} nad you will pay 10 dollars ticket.")
elif age >= 2 and age <= 8:
    print(f"You are {age} and you will pay 2 dollars ticket.")
elif age >= 65:
    print(f"You are {age} and you can go for free.")
elif age <=1:
    print(f"You are infant of age:{age} and you can go fr free.")


