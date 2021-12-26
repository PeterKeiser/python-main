# bouncer

# ask for age
# age = input("How old are you?: ")
# if age != "":
#     if int(age) >= 18 and int(age) < 21:
#         print("You can enter, however you have to wear a wristband.")
#     # 18-19  wristband
#     # 21+ drink, normal entry
#     elif int(age) >=21:
#         print("You can enter.")
#     # too young, sorry 
#     else:
#         print("You can't enter, littel one ;o).")
# else:
#     print("You have not enter anything.")
# ========================================================================
    # ask for age
age = input("How old are you?: ")
if age:
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, however you have to wear a wristband.")
    # 18-19  wristband
    # 21+ drink, normal entry
    elif int(age) >=21:
        print("You can enter.")
    # too young, sorry 
    else:
        print("You can't enter, littel one ;o).")
else:
    print("You have not enter anything.")