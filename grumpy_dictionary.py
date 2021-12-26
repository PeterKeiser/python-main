# grumpy_dictionary

class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}? Well, it aint here.")

    def __setitem__(self, key, value):
        print("You want to chage the dictionary?")
        print("OK, fine...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("No it aint here")
        return False





data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data["city"] = "Tokyo"
print(data)
"city" in data 








# d = GrumpyDict({"name": "Yoko", "city": "New Tork"})
# print(d)