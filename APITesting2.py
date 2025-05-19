import requests


url = 'https://en.wikipedia.org/w/api.php'
while True:
    lookup = input('enter a search term: ')
    parameters = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'explaintext': True,
        'titles': lookup,
    }

    response = requests.get(url, params=parameters)
    
    if next(iter(response.json()['query']['pages'])) == '-1':
        print('not a real page try again')
    elif next(iter(response.json()['query']['pages'].values()))['extract'] == "":
        print('no text found')
    else:
        data = response.json()
        break

print('page found')


text = next(iter(data['query']['pages'].values()))['extract']
#print(text)
TheDictionary = {'Introduction': []}
text = text.split('\n')
print(type(text))
sectionNum = 0
for line in text:
    if (line.startswith('==') or line.startswith('===')) and (line.endswith('==') or line.endswith('===')):
        line = line.strip('=')
        TheDictionary[line] = []
        sectionNum += 1
    else:
        key = list(TheDictionary.keys())[sectionNum]
        TheDictionary[key].append(line)
print(TheDictionary)