import re 

def regex_search(pokemon_list, pattern):
    results = []

    for pokemon in pokemon_list:

        if re.search(pattern, pokemon.name, re.IGNORECASE):
            results.append(pokemon)

            return results