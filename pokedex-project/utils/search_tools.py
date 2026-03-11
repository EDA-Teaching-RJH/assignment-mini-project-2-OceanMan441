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
    Searches Pokémon by type(s), ignoring order, spaces, and case.
    Use '/' as a separator in input, e.g., 'Fire/Flying'.
    """

    search_set = set(t.strip().capitalize() for t in search_type.split('/'))

    results = []
    for pokemon in pokemon_list:
        pokemon_set = set([t.strip().capitalize() for t in pokemon.type])  

        if pokemon_set == search_set:
            results.append(pokemon)

    return results
