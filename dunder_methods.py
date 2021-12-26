# dunder_methods

# _name
# __name
# __name__


class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like turtels"
        self.__lol = "HAHAHAHAHA"

p = Person()

print(p.name)
print(p._secret)
# print(p.__msg)
# print(dir(p))
print(p._Person__msg)
print(p._Person__lol)





