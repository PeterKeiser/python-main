# csv_dictwriter


from csv import DictWriter, DictReader

# with open("example.csv", "w") as file:
#     headers = ["Character", "Move"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Character": "Ryu",
#         "Move": "Hadouken"
#     })


def cm_to_in(cm):
    return float(cm) * 0.393701

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for fighter in fighters:
        csv_writer.writerow({
            "Name": fighter["Name"],
            "Country": fighter["Country"],
            "Height": cm_to_in(fighter["Height (in cm)"])
        })







