import requests

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()

# Use this JSON formatter to better visualize the JSON from the Pokemon website
# https://jsonformatter.org/json-viewer
poke = input("please enter the name of a pokemon")
pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/"+poke).json()
print(pokemon["name"])
print(pokemon)