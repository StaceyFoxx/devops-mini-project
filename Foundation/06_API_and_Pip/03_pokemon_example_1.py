"""
This API is called 'Pokéapi' pokeapi.co/
It gives access to data about Pokémons
This API is free and does not require any authentication!

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls

https://pokeapi.co/api/v2/pokemon/6/
"""

import requests

pokemon_number = input("What is the Pokemon's ID? ")

endpoint = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)  # note how we manupulate the url to request data!

response = requests.get(endpoint)
print(response)

pokemon = response.json()
print(pokemon)

