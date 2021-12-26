# bulk_insert

import sqlite3

conn = sqlite3.connect("my_friends.db")
# create cursor
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)
]

# for person in people:
#     insert that one person...

# c.executemany("INSERT INTO friends VALUES (?,?,?)",people)

for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print("INSERTING NOW!!!")




# c.execute(query,data)
# commit changes
conn.commit()
conn.close()

