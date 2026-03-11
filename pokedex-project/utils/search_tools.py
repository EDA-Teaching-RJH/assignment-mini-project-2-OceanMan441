import re

def regex_search(pokemon_list, pattern):
    """
    Searches the list of Pokemon using a regex pattern
    and returns all matching Pokemon.
    """

    results = []

    for pokemon in pokemon_list:

        if re.search(pattern, pokemon.name, re.IGNORECASE):
            results.append(pokemon)

    return results

def search_by_type(pokemon_list, search_type):
    """
    Searches the list of Pokémon by type(s), ignoring order, spaces, and case.
    search_type: string like "Fire, Flying"
    Returns a list of matching Pokémon.
    """

    search_set = set(t.strip().capitalize() for t in search_type.split(','))

    results = []
    for pokemon in pokemon_list:
        # Convert Pokémon's type string into a set
        pokemon_set = set(t.strip().capitalize() for t in pokemon.type.split(','))
        if pokemon_set == search_set:
            results.append(pokemon)

    return results
