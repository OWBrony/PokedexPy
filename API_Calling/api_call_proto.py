import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
RESULTS = None

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

def main():
    holder = get_data()
    place_data(holder)
    print_data(holder)

if __name__ == "__main__":
    main()