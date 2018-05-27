import config
import sqlite3

conn = sqlite3.connect('wiki.db')
cursor = conn.cursor()

cursor.execute("insert into questions values (Null, 'Test3!') ")
conn.commit()

cursor.execute("SELECT text FROM questions ")

results = cursor.fetchall()
for i in results:
    print(i[0])
    

conn.close()
