import sqlite3


conn = sqlite3.connect("my_friends.db")
cursor = conn.cursor()

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

# data = ("Paul", "McCartney", 32)
# query = "INSERT INTO friends VALUES (?,?,?)"
# cursor.execute(query, data)

# people = [
#     ("Roald", "Amundsen", 5),
#     ("Rosa", "Parks", 8),
#     ("Henry", "Hudson", 7),
#     ("Neil", "Armstrong", 7)]
# cursor.executemany("INSERT INTO friends VALUES (?,?,?)", people)

cursor.execute("SELECT * FROM friends")
print(cursor.fetchall())

conn.commit()
conn.close()


# sqlite3 {database.db}
# .tables
# .schema
# select * from table;
# .quit