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
