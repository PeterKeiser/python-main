# chicken_coop

class Chickens:
    total_eggs = 0
    allowed =["Partridge Silkie", "Speckeled Sussex"]
    def __init__(self, name, species):
        if species not in Chickens.allowed:
            raise ValueError(f"Only {species} is allowed.") 
        self.name = name
        self.species = species
        self.eggs = 0
    # def eggs(self):
    #     return self.eggs
    def lay_egg(self, amount):
        self.eggs += amount
        Chickens.total_eggs += amount
        return self.eggs
    # def total_eggs(self, amount):
    #     return Chickens.total_eggs

c1 = Chickens(name="Alice", species="Partridge Silkie")
c2 = Chickens(name="Amelia", species= "Speckeled Sussex")


print(c1.name)
print(c2.name)
print(c1.species)
print(c2.species)
# print(Chickens.total_eggs())
print(c1.eggs)
print(c2.eggs)
print(c1.lay_egg(2))
print(c2.lay_egg(3))
print(c1.eggs)
print(c2.eggs)

