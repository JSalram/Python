import mariadb

conn = None

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="sakila")
except mariadb.Error as e:
    print(e)
    exit()

cur = conn.cursor()

cur.execute("SELECT * FROM actor;")

for actor in cur:
    print(f"{actor[0]}. {actor[1]} {actor[2]}")
