# jokes

import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 2000!")
header = colored(header, color="magenta")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

# json_res = res.json()
# num_jokes = len(res["results"])
num_jokes = res["total_jokes"]
if num_jokes > 1:
    print(f"I have found {num_jokes} jokes about: {user_input}.")
    print(choice(res["results"])["joke"])
elif num_jokes == 1:
    print(f"There is ONE joke with: {user_input}") 
    print(res["results"][0]["joke"])
else:
    print(f"Sorry, souldn't find a joke with your term: {user_input}")


print(len(res["results"]))






