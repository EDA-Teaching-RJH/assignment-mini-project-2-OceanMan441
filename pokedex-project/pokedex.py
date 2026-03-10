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
    
    def list_by_type(self, type_name):
    
        results = []
        for pokemon in self.pokemon_list:
            if type_name.lower() in pokemon.type.lower():
                results.append(pokemon)

        return results