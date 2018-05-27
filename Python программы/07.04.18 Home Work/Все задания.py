print("1 задание:")
ABC = []
a = input("Введите 1 число: ")
ABC.append(a)
a = input("Введите 2 число: ")
ABC.append(a)
a = input("Введите 3 число: ")
ABC.append(a)
Tsum = int(int(ABC[0]) + int(ABC[1]) + int(ABC[2]))
Tsum = Tsum - int(min(ABC))
print(Tsum)

print("2 задание:")

Ans = int(0)
a = int(input("Сколько будет 2 + 2 "))
if a == 4:
    Ans = Ans + 1
a = int(input("Сколько будет 3 * 22 "))
if a == 66:
    Ans = Ans + 1
a = int(input("Сколько будет 100 + 2 "))
if a == 102:
    Ans = Ans + 1
a = int(input("Сколько будет 2 + 2 * 2 "))
if a == 6:
    Ans = Ans + 1
a = int(input("Сколько будет 3 + 3 * 2 "))
if a == 9:
    Ans = Ans + 1
print(Ans, "Ответов из 5 ")

ABC = []
print("3 задание:")
a = int(input("Введите число:"))
while(a != 0):
    ABC.append(a % 10)
    a = a / 10
ABC.reverse()
print(ABC)



print("4 задание:")
a = int(input("Введите число:"))
while(a != 0):
    ABC.append(a % 10)
    a = a / 10
print(max(ABC))



print("5 задание:")
myfile = open('text.txt' , 'r+')
print(myfile.name(), myfile.mode())
