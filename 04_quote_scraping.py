from random import choice
import requests
from bs4 import BeautifulSoup
from time import sleep

BASE_URL: str = "http://quotes.toscrape.com"

def scrape_quotes() -> list:
    all_quotes: list = []
    url: str = "/page/1"

    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parserpip")
        quotes: list = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })

        next_button: str = soup.find(class_="next")
        url: str = next_button.find("a")["href"] if next_button else None
        # sleep(2)
    return all_quotes


def start_game(quotes: list):
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
    quotes: list = scrape_quotes()
    start_game(quotes)