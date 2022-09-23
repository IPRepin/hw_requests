import requests
import pprint
import json

heroes_dict = {}
def halk():

    hero_url = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/332.json")
    data_name = hero_url.json()
    # pprint(data_name)
    name = data_name['name']

    heroe_powerstats = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/332.json')
    data_powerstats = heroe_powerstats.json()
    powerstats = data_powerstats["intelligence"]
    heroes_dict[name] = powerstats
    # print(f'{name} {powerstats}')
halk()


def cap():
    hero_url = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/149.json")
    data_name = hero_url.json()
    # pprint(data_name)
    name = data_name['name']

    heroe_powerstats = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/149.json')
    data_powerstats = heroe_powerstats.json()
    powerstats = data_powerstats["intelligence"]
    heroes_dict[name] = powerstats
    # print(f'{name} {powerstats}')

cap()

def  thanos():
    hero_url = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/655.json")
    data_name = hero_url.json()
    # pprint(data_name)
    name = data_name['name']

    heroe_powerstats = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/655.json')
    data_powerstats = heroe_powerstats.json()
    powerstats = data_powerstats["intelligence"]
    heroes_dict[name] = powerstats
    # print(f'{name} {powerstats}')

thanos()

def max_intelligence():
    heroes_val = heroes_dict.items()
    heroes_val_lst = list(heroes_val)
    kv = max(heroes_val_lst, key=lambda i: i[1])
    # print(kv)
    name = kv[0]
    intelligence = kv[1]
    print(f'{name} - {intelligence}')
max_intelligence()
