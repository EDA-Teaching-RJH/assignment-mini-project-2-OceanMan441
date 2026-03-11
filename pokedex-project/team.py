class Team:
    def __init__(self):
        self.team = []

    def add_pokemon(self, pokemon):
        if len(self.team) >= 6:
            print("Your team already has 6 Pokémon.")
            return 
        
        if pokemon in self.team:
            print("This Pokémon is already in your team.")
            return
        
        self.team.append(pokemon)
        print(f"{pokemon.name} added to your team.")

    def remove_pokemon(self, name):
        for pokemon in self.team:
            if pokemon.name.lower() == name.lower():
                self.team.remove(pokemon)
                print(f"{pokemon.name} removed from your team.")
                return
            
        print("Pokémon not found in your team.")

    def show_team(self):
        if not self.team:
            print("Your team is empty.")
            return
        
        print("\n--- Your Pokémon Team ---")

        for pokemon in self.team:
            print(pokemon.display_info())
            