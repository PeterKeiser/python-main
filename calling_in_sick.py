# calling in sick

from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(1,10)

calling_in_sick = None
if actually_sick == True and sick_days >=1:
    calling_in_sick = True
    print(f"calling in sick; actually sick: {actually_sick}, sick days: {sick_days}")
elif kinda_sick == True and hate_your_job == True and sick_days >=1:
    calling_in_sick = True
    print(f"calling in sick; kinda sick: {kinda_sick}, hate your job: {hate_your_job}, sick days: {sick_days} ") 
else:
    print("you have to go to work")

