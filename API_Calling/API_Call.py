import requests
import json

class Caller():
    def __init__(self):
        self.pokemon_name = ""
        self.first_ability = ""
        self.second_ability = ""
        self.hidden_ability = ""
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.spec_attack = 0
        self.spec_defense = 0
        self.speed = 0
        self. stat_total = (self.health + self.attack + self.defense +
        self.spec_attack + self.spec_defense + self.speed)
        self.sprite = None

    def check_data(self,name):
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

    def get_data(self, name):
        """This is to get the data for the pokemon the user wants.
        The user will either search or click on a pokemon.
        The function sould get a pokemon name passed in."""
        pokemon = name
        # check_data should correct the name of a pokemon that is passed in.
        # either dealing with names with special characters and/or lowering
        # the case of the name so it can be passed to the API.
        corrected = check_data(pokemon)
        response_API = requests.get(f"{BASE_URL}{corrected}")
        if not response_API:
            return
        else:
            data = response_API.json()
            # set the pokemon's data
            set_info(pokemon, data)
            return data
    
    def set_info(self, data):
        """This is to set all the info for the pokemon"""
        self.first_ability = data["abilities"][0]["ability"]["name"]
        if data["abilities"][1]["ability"]["name"]:
            self.second_ability = data["abilities"][1]["ability"]["name"]
        elif data["abilities"][1]["ability"]["is_hidden"] == "T":
            self.hidden_ability = data["abilities"][1]["ability"]["name"]
        if data["abilities"][2]["ability"]["is_hidden"] == "T":
            self.hidden_ability = data["abilities"][2]["ability"]["name"]
        self.sprite = data["sprites"]["front_default"]
        