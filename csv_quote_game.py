# csv_quote_game

# scraper of quotes

import requests 
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader


BASE_URL = "https://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, "r", encoding="UTF-8", newline = "") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game():
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here is the qote: ")
    print(quote["text"])
    print(quote["author"])
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses} \n")
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT!!!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here is a hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here is a hint: The initial of the author's first name is: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here is a hint: The initial of the author's last name is: {last_initial}")
        else:
            print(f"Sorry, you ran out of guesses. The answer was: {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again: y/n? ")
    if again.lower() in ("yes", "y"):
       return start_game(quotes)
    # play again
    else:
        print("OK, goodbye!")
quotes = read_quotes("quotes.csv") 
start_game()
    

    



