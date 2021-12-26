# select

import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor
c = conn.cursor()
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
# for result in c:
#     print(result)

print(c.fetchall())
# print(c.fetchone())

# commit changes
conn.commit()
conn.close()
# c.commit()
# c.close()



