import os
from pokedex import Pokedex 
from utils.search_tools import regex_search, search_by_type
from team import Team

def main(): 

    pokedex = Pokedex()
    team = Team()

    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "pokemon151.csv")

    pokedex.load_pokemon(csv_path)

    while True: 

        print("\n--- POKEDEX ---")
        print("1. Search Pokémon by name")
        print("2. List Pokémon by type")
        print("3. Regex search")
        print("4. Add Pokémon to team")
        print("5. Remove Pokémon from team")
        print("6. Show team")
        print("7. Exit")

        choice = input("Choose option: ")
    
        if choice == "1":

            name = input("Enter Pokémon name: ")
            pokemon = pokedex.search_pokemon_by_name(name)

            if pokemon:
                pokemon.display_info()
            else:
                print("Pokémon not found.")

        elif choice == "2":
           
            type_input = input("Enter Pokémon type(s) (comma separated if multiple): ")
            pokemon_list = search_by_type(pokedex.pokemon_list, type_input)

            if pokemon_list:
                for pokemon in pokemon_list:
                    pokemon.display_info()
            else:
                print("No Pokémon found with that type combination.")

        
        elif choice == "3":
            pattern = input("Enter regex pattern: ")
            results =  regex_search(pokedex.pokemon_list, pattern)
           
            for p in results:
                print(p.name)

        elif choice == "4":
            name = input("Enter Pokémon name to add: ")
            pokemon = pokedex.search_pokemon_by_name(name)

            if pokemon:
                team.add_pokemon(pokemon)
            else:
                print("Pokémon not found.")


        elif choice == "5":
            name = input("Enter Pokémon name to remove: ")
            team.remove_pokemon(name)

        
        elif choice == "6":
            team.show_team()


        elif choice == "7":
            print("Exiting Pokedex. Goodbye!")
            break
    
if __name__ == "__main__":
     main()


