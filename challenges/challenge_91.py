#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # print(pokeapi)
    
    # print(pokeapi['sprites']['front_default'])
    
    # for move in pokeapi['moves']:
        # print(move["move"]["name"])
   
    print(len(pokeapi['game_indices']))

    ## BONUS WITH LOOP
    version_count = 0
    for version in pokeapi['game_indices']:
        version_count += 1

    print(version_count)

main()

