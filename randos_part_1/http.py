import requests
import pyfiglet
import termcolor
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="magenta")
print(header)

user_input = input("Let me tell you a joke! Give me a topic: ")
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()
results: dict = response_json["results"]
total_jokes: int = response_json["total_jokes"]

if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {user_input}. Here's one:\n",
        choice(results)['joke']
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {user_input}. Here it is:\n",
        results[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
