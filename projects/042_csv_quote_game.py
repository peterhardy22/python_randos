import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL: str = "http://quotes.toscrape.com"


def read_quotes(filename):
    """This function reads the quotes from a csv file and returns them as a list."""
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes: list):
    """This function allows the user to guess who said a quote with a number of guesses and hints along the way."""
    quote: dict = choice(quotes)
    remaining_guesses: int = 4
    guess: str = ""

    while guess.lower() != quote["author"].lower():
        guess = input(
            f"Who said this quote? Guesses remaing: {remaining_guesses}\n")
        guess -= 1
        if guess.lower() == quote["author"].lower():
            print("You guessed it correctly!!!")
            break
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date: str = soup.find(class_="author-born-date").get_text()
            birth_place: str = soup.find(class_="author-born-location").get_text()
            print(
                f"Here's a hint: The author was born on {birth_date} {birth_place}.")
        elif remaining_guesses == 2:
            print(
                f"Here's a hint: The author's first name starts with {quote['author'][0]}.")
        elif remaining_guesses == 1:
            last_initial: str = quote['author'].split(" ")[1][0]
            print(
                f"Here's a hint: The author's last name starts with {last_initial}.")
        else:
            print(
                f"Sorry you ran out of guesses. The answer was {quote['author']}.")

    again: str = ""
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again: str = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Ok, ta ta for now!")


if __name__ == "__main__":
    quotes: list = read_quotes("quotes.csv")
    start_game(quotes)