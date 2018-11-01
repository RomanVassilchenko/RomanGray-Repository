import sqlite3

conn = sqlite3.connect("botdb.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM questions") # cursor.execute("SELECT text FROM questions") выводит текст
#cursor.execute("SELECT text FROM questions WHERE id = 2") Выводит текст с id 2
print(cursor.fetchall()) # print(cursor.fetchall()[0][0]) Выводит индекс 

conn.close()
