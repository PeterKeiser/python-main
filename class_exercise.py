# class_exercise

class Vehicle:
    pass

vehicle1 = Vehicle()
vehicle2 = Vehicle()

car = vehicle1
boat = vehicle2


class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c1 = Comment("davey123", "lol you are so silly", 3)
c2 = Comment("pete4", "nice")

print(c1.username, c1.text, c1.likes)
print(c2. username, c2.text)
    





    



