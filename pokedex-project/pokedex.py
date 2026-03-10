import csv
from fileinput import filename
from py_compile import main 
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
