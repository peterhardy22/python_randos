import sqlite3


conn = sqlite3.connect("my_friends.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
conn.commit()
conn.close()


# sqlite3 {database.db}
# .tables
# .schema
# .quit