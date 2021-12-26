# update_users2

import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
    return f"Users updated: {count}"


print(update_users("Grace", "Hopper", "Hello", "World"))
print(update_users("Colt", "Steele", "Boba", "Feet"))
print(update_users("Not", "Here", "Still", "not Here"))

