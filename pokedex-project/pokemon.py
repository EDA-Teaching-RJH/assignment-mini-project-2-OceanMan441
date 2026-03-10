class Pokemon:

    def __init__(self, id, name, type, species, height, weight, habitat, description):
        self.id = id
        self.name = name 
        self.type = type
        self.species = species 
        self.height = height
        self.weight = weight
        self.habitat = habitat
        self.descrition = description 

    def display_info(self):

        return f"""

ID: {self.id}
Name: {self.name}
Type: {self.type}
Species: {self.species}
Height: {self.height}
Weight: {self.weight}
Habitat: {self.habitat}

Description:
{self.description}
"""
