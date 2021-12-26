# week_generator

def week_generator():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day


day = week_generator()
print(next(day))


for num in day:
    print(num)



