import sqlite3

# conn = sqlite3.connect("my_friends.db")
# cursor = conn.cursor()

# Creates table.
# cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# insert_query = '''INSERT INTO friends 
#                     VALUES ('Harrison', 'George', 64)'''
# cursor.execute(insert_query)

# BAD DONT DO THIS!
# form_first = "Ringo"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# form_first = "John"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# cursor.execute(query, (form_first,))

# data: tuple(str, str, int) = ("Paul", "McCartney", 32)
# query: str = "INSERT INTO friends VALUES (?,?,?)"
# cursor.execute(query, data)

# people: list[(str, str, int)] = [
#     ("Roald", "Amundsen", 5),
#     ("Rosa", "Parks", 8),
#     ("Henry", "Hudson", 7),
#     ("Neil", "Armstrong", 7)]
# cursor.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# `cursor.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
# print(cursor.fetchone())`

# conn.commit()
# conn.close()


# sqlite3 {database.db}
# .tables
# .schema
# select * from table;
# .quit


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Set up users table and create test users.
# query = "CREATE TABLE users (username TEXT, password TEST)"
# cursor.execute(query)
# users_list: list[(str, str    q)] = [
#     ("Pedro","dn823wfndjfSDF"),
#     ("Cdub", "hf42MVC:?weh@>2"),
#     ("JaMickie", "shimmytutu")
# ]
# cursor.executemany("INSERT INTO users VALUES (?,?)", users_list)
u_name: str = input("Please enter your username: ")
p_word: str = input("Please enter your password: ")

# query = f"SELECT * FROM users WHERE username = '{u_name}' AND password = '{p_word}'"
      #  "SELECT * FROM users WHERE username = 'Pedro' AND password = '' OR 1=1 --'" -> SQL injection that is always TRUE.
query = f"SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (u_name, p_word))

result = cursor.fetchone()
if(result):
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()