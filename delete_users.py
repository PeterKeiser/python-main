# delete_users

import csv

def delete_users(first, last):
    with open("users.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first and row[1] == last:
                csv_writer.writerow(["",""])
                count += 1
            else:
                csv_writer.writerow(row)
    return f"Users deleted: {count}"




print(delete_users("Alan", "Turing"))
print(delete_users("Colt", "Steele"))
# print(delete_users("Not", "Here"))