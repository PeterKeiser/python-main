# RPG

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self. level = level
    
class NPC(Character):
    def __init__(self, name, hp, level, phrase):
        super().__init__(name, hp, level)
        self.phrase = phrase
        

    def speak(self):
        return f"When player interacts with the caracter, the caracter says: {self.phrase}"


Bill = NPC("Bill", 100, 3, "I like your shoes...")
print(Bill.speak())
Peter = NPC("Peter", 100, 4, "I like your shoes and skirt")
print(Peter.speak())
    

