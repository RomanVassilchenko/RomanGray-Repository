phones = {"Вася":"77777777777","Петя":"77776666666","Маша":"77775555555","Котик":"77774444444","Рыбка":"77773333333"}
name = input("Введите Имя")
number =int(input("Введите Номер"))
phones[name]=number
print(phones)


'''
phones.fromkeys(name,phones)
phones.update(name,phones)
'''
