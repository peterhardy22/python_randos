from random import choice
import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL: str = "http://quotes.toscrape.com"


def scrape_quotes() -> list:
    """This function scrapes quotes from a quote scraping website."""
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
        sleep(1)
    return all_quotes


def write_quotes(quotes: list):
    """This function writes quotes to a csv file."""
    with open("quotes.csv", "w") as file:
        headers: list = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, filednames=headers) 
        csv_writer.writeheader()

        for quote in quotes:
            csv_writer.writerow(quote)

quotes: list = scrape_quotes()
write_quotes(quotes)