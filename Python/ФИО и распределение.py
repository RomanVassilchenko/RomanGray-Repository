a = input("Введите ФИО ")
Name = ""
Vamilia = ""
Otchestvo = ""
r = int(0)
while a[r] == " ":
    r = r + 1
r = r + 1
t = int(r)
while a[r] != " ":
    t = t + 1
t = t + 1
for i in range (r , t):
    Name = Name + a[i]
print (Name)
