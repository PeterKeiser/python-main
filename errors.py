# errors

# raise ValueError("invalid value")

# print("hi")
# colorize("hi", "red")

# def colorize(text, colour):
#     colours = ("cyan", "yellow", "blue", "green", "magenta")
#     if type(colour) is not str:
#         raise TypeError("colour must be a string")
#     if type(text) is not str:
#         raise TypeError("text must be a string")
#     if colour not in colours:
#         raise ValueError("colour is invalid colour") 
#     print(f"Printed {text} in {colour}")


# # colorize("hello", "red")
# colorize([], "cyan")


# foobar
# try:
#     foobar
# except NameError as err:
#     print(err)

# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")



def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Rickey"}
# print(get(d, "name"))
print(get(d, "city"))



