import requests
from random import choice
from pyfiglet import figlet_format 
from termcolor import colored
header = figlet_format("Dad Joke 5000")
header = colored(header, color="cyan")
print(header)

user_input = input("What would you like to search for? ")
url = "https://www.icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term":user_input}
).json()

#json_res = res.json()
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} about {user_input}. Here's one: ")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print("I found one joke about {user_input}")
	print(results[0]['joke'])
else:
	print(f"Sorry, couldn't find a joke with your term: {user_input}")