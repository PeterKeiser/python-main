# scream

from csv import reader, writer

# with only 1 file open at a time
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
      # data converted to list and saved to avariable
#     fighters = [[s.upper() for s in row] for row in csv_reader]
#     # for row in fighters:
#     #     print(row)
# with open("screaming_fighters.csv", "w") as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)

# using nested with statements
with open("fighters.csv") as file:
    csv_reader = reader(file)
    # fighters = [[s.upper() for s in row] for row in csv_reader]
    with open("screaming_fighters.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper()for s in fighter])


