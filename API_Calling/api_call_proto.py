import requests
import json
import firebase_admin
from firebase_admin import credentials

ref = "C:/Users/bgfra/Downloads/pokedexpy-firebase-adminsdk-2s83s-3c54b27850.json"

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
RESULTS = None

cred_obj = firebase_admin.credentials.Certificate(ref)
default_app = firebase_admin.initialize_app(cred_obj, {
	'https://pokedexpy-default-rtdb.firebaseio.com/':databaseURL
	})

# def convert_to_json(response):
#     return json.loads(response)

#     pass

def get_data():
    pokemon = input("What pokemon do you want? ")
    response_API = requests.get(f"{BASE_URL}{pokemon}")
    data = response_API.text
    holder = json.loads(data)
    # parse_json
    return holder

def place_data(data):
    RESULTS = data

def print_data(data):
    print(data["abilities"])

def send_data(data):
    pass

def main():
    holder = get_data()
    place_data(holder)
    print_data(holder)

if __name__ == "__main__":
    main()