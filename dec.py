# dec

def be_polite(fn):
    def wrapper():
        print("What a plasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")

@be_polite
def rage():
    print("I hate you!")

greet()
rage()


# greet = be_polite(greet)
# polite_rage = be_polite(rage)

# print(rage())
# print(polite_rage())

# print(greet())
# print(greet())
# print(greet())



