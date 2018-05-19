'''
f = open('test.txt','r+') #писать полный путь если они е в одной
f.write('Мой первый \nкак')

f.close()

f = open('test.txt' ,'r+')
print(f.read())

f.close()

#""" """ режим многострочного ввода

'''
with open ('test.txt','r+') as f:
    f.write("""
как
это
работает?
""")
    f.close()


with open('test.txt','r+')  as f:
    print(f.read())
    f.close()

