'''
Script para mostrar os pokemons da primeira geração

'''
import requests
URL = 'https://pokeapi.co/api/v2/generation/2'
req = requests.get(URL)
if req.status_code == 200:
    dados = req.json()
    for pokemon in dados['pokemon_species']:
        print(pokemon['name'])

if req.status_code == 404:
    print('Não encontrado')