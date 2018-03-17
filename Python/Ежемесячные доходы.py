month = int(input("Введите сколько месяцев вы работали без зарплаты "))
sum = int()
for i in range (1 , month + 1):
    money = int(input("Введите доход "))
    sum = sum + money
print(sum / month)
