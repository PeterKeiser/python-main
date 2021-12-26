# find_user

import csv

def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            # print(index, row)
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first_name} {last_name} not found."





print(find_user("Colt", "Steele"))
# find_user("Alan", "Turing")
print(find_user("Not", "Sure"))




