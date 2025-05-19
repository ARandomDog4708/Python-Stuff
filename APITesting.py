import requests 
pokemonPicked = False
while not pokemonPicked:

    pokemon_name = input('what pokecreature you want ').lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    

    response = requests.get(url)
    
    if response.status_code == 200:
        pokemonPicked = True
        data = response.json()
    elif response.status_code == 404:

        print('try again with a different pokecreature')
print('pokecreature found')
print('\n')
print(f'pokecreature name:', data['name'].title())
print('\n')
types = [type['type']['name'] for type in data['types']]
print('\n')
print('type(s):', ','.join(types))
print('here da stats aboput your pokecreature')
for stat in data['stats']:
    stat_name = stat['stat']['name'].title()
    baseStat = stat['base_stat']
    print(f'{stat_name}: {baseStat}')
    

