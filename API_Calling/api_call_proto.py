import requests
import json
import firebase_admin
from firebase_admin import credentials

ref = "C:/Users/bgfra/Downloads/pokedexpy-firebase-adminsdk-2s83s-3c54b27850.json"

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
RESULTS = None

pokemon_name = ""
first_ability = ""
SPRITE = ""
HEALTH = 0
ATTACK = 0
DEFENCE = 0
SPEC_ATTACK = 0
SPEC_DEFENCE = 0
SPEED = 0

def check_data(name):
    if name.lower() == "farfetch'd":
        return "farfetchd"
    elif name.lower() == "mr. mime" or name.lower() == "mr.mime" or name.lower() == "mr mime":
        return "mr-mime"
    elif name.lower() == "nidoran f" or name.lower() == "nidoran ♀" or name.lower() == "nidoran♀" or name.lower() == "nidoran female":
        return "nidoran-f"
    elif name.lower() == "nidoran m" or name.lower() == "nidoran ♂" or name.lower() == "nidoran♂" or name.lower() == "nidoran male":
        return "nidoran-m"
    else:
        return name.lower()

def get_data():
    pokemon = input("What pokemon do you want? ")
    corrected = check_data(pokemon)
    response_API = requests.get(f"{BASE_URL}{corrected}")
    if not response_API:
        return
    else:
        data = response_API.json()
        # set the pokemon's data
        return data

def set_info(data):
    SPRITE = data["sprites"]["front_default"]
    holder1 = data["stats"][0]["base_stat"]
    holder2 = data["stats"][1]["base_stat"]
    holder3 = data["stats"][2]["base_stat"]
    holder4 = data["stats"][3]["base_stat"]
    holder5 = data["stats"][4]["base_stat"]
    holder6 = data["stats"][5]["base_stat"]
    HEALTH = holder1
    ATTACK = holder2
    DEFENCE = holder3
    SPEC_ATTACK = holder4
    SPEC_DEFENCE = holder5
    SPEED = holder6

def place_data(name,data):
    RESULTS = data

def _print_data(data):
    if not data:
        print("No Data")
    else:
        print(data["abilities"][0]["ability"]["name"])
        print(HEALTH)
        print(ATTACK)
        print(DEFENCE)
        print(SPEC_ATTACK)
        print(SPEC_DEFENCE)
        print(SPEED)
        # print(f"{data['stats'][0]['base_stat']['stat']['name']}: {data['stats'][0]['stat']}")
        
        # ["abilities"][0]["ability"]["name"]

def send_data(data):
    pass

def main():
    holder = get_data()
    if holder:
        set_info(holder)
    # place_data(holder)
        _print_data(holder)

if __name__ == "__main__":
    main()