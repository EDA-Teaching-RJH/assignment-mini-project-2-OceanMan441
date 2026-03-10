import unittest
from pokedex import Pokedex

class TestPokedex(unittest.Testcase): 

    def setUp(self):
        self.pokedex = Pokedex()
        self.pokedex.load_pokemon("data/pokemon151.csv")

    def test_search_pikachu(self):
        pokemon = self.pokedex.search_by_name("Pikachu")
        self.assertEqual(pokemon.name, "Pikachu")

    def test_type_search(self):

        results = self.pokedex.list_by_type("Electric")
        self.assertTrue(len(results) > 0)

    if __name__ == "__main__":
        unittest.main()