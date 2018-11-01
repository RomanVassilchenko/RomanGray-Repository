start =  int(input("Введите старт "))
end =  int(input("Введите конец "))
step = int(input("Введите шаг "))
if(end < start):
    print("Error")
for i in range (1 , end + 1 - start, step):
    print (i)
