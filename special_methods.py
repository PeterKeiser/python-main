# special_methods

class Human:
    def __init__(self, height, name="somebody"):
        self.height = height
        self.name = name

    def __len__(self):
        return self.height

    def __repr__(self):
        return self.name

Colt = Human(60, "Colt")

print(len(Colt))
print(Colt)






