import requests
import json
import pandas as pd

def get_pokemon():
  url = 'https://pokeapi.co/api/v2/pokemon/?limit=-1'
  response = requests.get(url).text
  document = json.loads(response)  
  return document['results']

pokemon = get_pokemon()
df = pd.DataFrame(pokemon)

def get_pokemon_document(url):
    return requests.get(url).text

df['result'] = df.url.apply(get_pokemon_document)

def get_height(result):
    document = json.loads(result)
    return document['height']

df['height'] = df.result.apply(get_height)

height = df[['name', 'height']]
height.nlargest(4, 'height')