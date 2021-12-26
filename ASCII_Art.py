# ASCII_Art


# # install pyfiglet
# # python -m pip install pyfiglet

# import pyfiglet
# from termcolor import colored
# valid_colours = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
# #   Available text colors:
#             # red, green, yellow, blue, magenta, cyan, white.

# msg = input("What would you like to print? ")
# colour = input ("What colour? ")
# if colour not in valid_colours:
#     colour = "magenta"


# ascii_art = pyfiglet.figlet_format(msg)
# colored_ascii_art = colored(ascii_art, color=colour)
# print(ascii_art)
# print(colored_ascii_art)


from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
    valid_colours = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

    if color not in valid_colours:
        color = "magenta"
    
    ascii_art = figlet_format(msg)
    colored_ascii_art = colored(ascii_art, color=colour)
    print(ascii_art)
    print(colored_ascii_art)

msg = input("What would you like to print? ")
colour = input ("What colour? ") 
print(print_art(msg, colour))







