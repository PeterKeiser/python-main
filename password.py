# password

import sqlite3
conn = sqlite3.connect("user.db")

# query = "CREATE TABLE users (username TEXT, password TEXT)"
# c.execute("CREATE TABLE users (username TEXT, password TEXT)")
# insert_query = '''INSERT INTO users 
#                     VALUES('Colt', 'frt86ut43')'''

u = input("please enter your username...")
p = input("please enter your password...")
#BAD Idea!!!                                                            ' OR 1=1--
# query = f"SELECT * FROM users WHERE username = '{u}' AND password = '{p}'"
c = conn.cursor()
query = f"SELECT * FROM users WHERE username =? AND password =?"

c.execute(query,(u,p))

result = c.fetchone()
if result:
    print("Welcome back")
else:
    print("Failed login")


conn.commit()
conn.close()


