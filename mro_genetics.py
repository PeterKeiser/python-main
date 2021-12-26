# mro_genetics

# class Mother:
#     def __init__(self, eye_colour, hair_colour, hair_type):
#         self.eye_colour = eye_colour
#         self.hair_colour = hair_colour
#         self.hair_type = hair_type


class Mother:
    def __init__(self):
        self.eye_colour = "brown"
        self.hair_colour = "dark brown"
        self.hair_type = "curly"

# class Father:
#     def __init__(self):
#         pass

class Father:
    def __init__(self):
        self.eye_colour = "blue"
        self.hair_colour = "blond"
        self.hair_type = "straight"

# class Child(Mother):
#     def __init__(self, eye_colour, hair_colour, hair_type):
#         super().__init__(eye_colour,hair_colour, hair_type)

class Child(Mother, Father):
    pass

child = Child()
print(child.eye_colour)
print(child.hair_colour)
print(child.hair_type)
help(child)

