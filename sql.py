import sqlite3


conn = sqlite3.connect("my_friends.db")
cursor = conn.cursor()

# Creates table.
# cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

insert_query = '''INSERT INTO friends 
                    VALUES ('Harrison', 'George', 64)'''
cursor.execute(insert_query)
conn.commit()
conn.close()


# sqlite3 {database.db}
# .tables
# .schema
# select * from table;
# .quit