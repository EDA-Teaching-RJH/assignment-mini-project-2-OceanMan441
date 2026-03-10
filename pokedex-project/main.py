from pokedex import Pokedex 
from utils.search_tools import regex_search

def main(): 

    pokedex = Pokedex()

    pokedex.load_pokemon("./data/pokemon151.csv")

    while True: 

        print("\n--- POKEDEX ---")
        print("1. Search Pokémon by name")
        print("2. List Pokémon by type")
        print("3. Regex search")
        print("4. Exit")

        choice = input("Choose option: ")
    
        if choice == "1":

            name = input("Enter Pokémon name: ")
            pokemon = pokedex.search_pokemon_by_name(name)

            if pokemon:
                pokemon.display_info()

            else:
                print("Pokémon not found.")

        elif choice == "2":
            type = input("Enter Pokémon type: ")
            pokemon_list = pokedex.list_pokemon_by_type(type)

        if pokemon_list:
            for pokemon in pokemon_list:
                print(pokemon.display_info())
            else:
                print("No Pokémon found with that type.")
        elif choice == "3":
            pattern = input("Enter regex pattern: ")
            results =  regex_search(pokedex.pokemon_list, pattern)
           
            for p in results:
                print(p.name)

        elif choice == "4":

                print("Exiting Pokedex. Goodbye!")
                break
        else:
                print("Exting Pokedex. Goodbye!")
    

if __name__ == "__main__":
     main()
