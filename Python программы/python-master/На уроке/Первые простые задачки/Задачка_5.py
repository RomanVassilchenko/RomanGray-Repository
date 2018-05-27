
s = input('Введите Ф.И.О.')
for i in s:
    if i ==" ":
        print('ooo')
        for i in s:
            if i ==" ":
                s.remove(i)
print(s.title())

