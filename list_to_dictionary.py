# list to dictionary

person = [["name", "Jared"], ["job", "musician"], ["city", "Bern"]]

print(person)

# answer = {k:l[0], v:l[1] for l in person()}
answer = {thing[0]: thing[1] for thing in person}
print(person)

answer = {k:v for k,v in person}
print(answer)

answer = dict(person)
print(answer)