how = int(input("Введите количество учащихся "))
b = []
r = int(0)
a = []
for i in range (0 , how):
    q = input()
    a.append(q)

time = input()
for i in range (0 , len(time)):
    if time[i] != " ":
        b.append(time[i])
cnt = int(0)
print("Пришли:")
for i in range (0 , len(b)):
    if(b[i] == "1"):
        print (a[i])
        cnt = cnt + 1
print(cnt)
cnt = int(0)
print("Не пришли:")
for i in range (0 , len(b)):
    if(b[i] == "0"):
        print (a[i])
        cnt = cnt + 1
print(cnt)
cnt = int(0)
print("Опоздали:")
for i in range (0 , len(b)):
    if(b[i] == "2"):
        print (a[i])
        cnt = cnt + 1
print(cnt)
cnt = int(0)
