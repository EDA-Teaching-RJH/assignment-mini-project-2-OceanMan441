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
                    row["Id"],
                    row["Name"],
                    row["Type"],
                    row["Species"],
                    row["Height"],
                    row["Weight"],
                    row["Habitat"],
                    row["Description"]
                )
                self.pokemon_list.append(pokemon)
