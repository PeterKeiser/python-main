# add_user

import csv

def add_user(first_name, last_name):
    with open("users.csv", "a", newline="", encoding = "UTF-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])


add_user("Alan", "Turing")
add_user("Peter", "Muller")
add_user("John", "Vangelis")
add_user("John", "Vangelis")


