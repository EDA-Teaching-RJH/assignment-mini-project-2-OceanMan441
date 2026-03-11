class Pokemon:

    def __init__(self, id, name, type_str, species, height, weight, habitat, description):
        self.id = id
        self.name = name 
        self.type = [t.strip().capitalize() for t in type_str.split(', ')]
        self.species = species 
        self.height = height
        self.weight = weight
        self.habitat = habitat
        self.description = description

    def display_info(self):
        type_display = ", ".join(self.type)

        print (f"""

    ID: {self.id}
    Name: {self.name}
    Type: {self.type}
    Species: {self.species}
    Height: {self.height}
    Weight: {self.weight}
    Habitat: {self.habitat}
    Description: {self.description}
    """)