class Pokemon:

    def __init__(self, id, name, type, species, height, weight, habitat, description):
        self.id = id
        self.name = name 
        self.type = type
        self.species = species 
        self.height = height
        self.weight = weight
        self.habitat = habitat
        self.descrition = description 

    def display_info(self):

        return f"""

ID: {self.id}
Name: {self.name}
Type: {self.type}
Species: {self.species}
Height: {self.height}
Weight: {self.weight}
Habitat: {self.habitat}

Description:
{self.description}
"""

import csv 

from pokemon import Pokemon

class Pokedex:

    def __init__(self):
        self.pokemon_list = []

    def load_pokemon(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:

                pokemon = Pokemon(
                    row["id"],
                    row["name"],
                    row["type"],
                    row["species"],
                    row["height"],
                    row["weight"],
                    row["habitat"],
                    row["description"]
                )
                self.pokemon_list.append(pokemon)

    def search_by_name(self, name):
        for pokemon in self.pokemon_list:
            if pokemon.name.lower() == name.lower():
                return pokemon 
            
        return None
    