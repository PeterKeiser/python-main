# extract_full_name

names = [{"first": "Elie", "last": "Schoppik"}, {"first":"Colt", "last": "Steele"}]

def extract_full_name(names):
    return list(map(lambda name: "{} {}".format(name["first"], name["last"]), names))


print(extract_full_name(names))
