# print_users

import csv

def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            print(f"First Name:{row['First Name']}, Last Name: {row['Last Name']}.")
            # print("{} {}".format(row['First Name'], row['Last Name']))
    


print_users()

