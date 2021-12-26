# else_finallt

# try:
#     num = int(input("please enter a number: "))
# except: 
#     print("That's not a number!")
# else:
#     print("I'M IN THE ELESE")
#     print(num)
# finally:
#     print("Runs always!!!")
#     print(num)


while True:
    try:
        num = int(input("please enter a number: "))
    except: 
        print("That's not a number!")
    else:
        print("Good job, you entered a number")
        print(num)
        break
    finally:
        print("Runs always!!!")
        print(num)
print("REST OF GAME LOGIC RUNS!")










