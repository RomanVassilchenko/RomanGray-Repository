f = open("text.txt", "r+")
#Считываем файл test.txt. Варианты r (Читать) r+ (Читать и писать)
# w (Писать) w+ (Писать и читать) a(Добавить в конец)

f.write("""
Test
Text
123456
""")
f.close()
f = open("text.txt" , "r+")
print(f.read()) #Вывести , что в текстовом файле было
f.close() #Закрыть файл
# f.seek переносит в начало


'''
with open("text.txt", "r+") as f:
    f.write("""
Test
Text
123456
    """)
    f.close()
with open("text.txt" , "r+") as f:
    print(f.read())
    f.close()
'''
