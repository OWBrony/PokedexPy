import requests
import json
import firebase_admin
from firebase_admin import credentials

ref = "C:/Users/bgfra/Downloads/pokedexpy-firebase-adminsdk-2s83s-3c54b27850.json"

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
RESULTS = None

pokemon_name = ""
first_ability = ""
sprite = ""

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
        set_info(data)
        return data

def set_info(data):
    sprite = data["sprites"]["front_default"]
    pass

def place_data(name,data):
    RESULTS = data

def _print_data(data):
    if not data:
        print("No Data")
    else:
        print(f"{data['stats'][0]['stat']['name']}: {data['stats'][0]['stat']['base_stat']}")
        print(data["abilities"][0]["ability"]["name"])
        # ["abilities"][0]["ability"]["name"]

def send_data(data):
    pass

def main():
    holder = get_data()
    # place_data(holder)
    _print_data(holder)

if __name__ == "__main__":
    main()