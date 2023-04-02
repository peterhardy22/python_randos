import requests
from bs4 import BeautifulSoup
from time import sleep


all_quotes: list = []
base_url: str = "http://quotes.toscrape.com"
url: str = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    print(type(res))
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
