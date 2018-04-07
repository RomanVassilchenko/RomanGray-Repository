a = int(input())
b = input()
c = int(input())
if b == '+':
    f = open("Time.txt", "a")
    d = str(a) + ' ' + str(b) + ' ' + str(c) + ' = ' + str(a + c)+ '\n'
    
    f.write(d)
    f.close()
if b == '-':
    f = open("Time.txt", "a")
    d = str(a) + ' ' + str(b) + ' ' + str(c) + ' = ' + str(a - c)+ '\n'
    f.write(d)
    f.close()
if b == '*':
    f = open("Time.txt", "a")
    d = str(a) + ' ' + str(b) + ' ' + str(c) + ' = ' + str(a * c)+ '\n'
    f.write(d)
    f.close()
if b == '/':
    f = open("Time.txt", "a")
    d = str(a) + ' ' + str(b) + ' ' + str(c) + ' = ' + str(a / c) + '\n'
    f.write(d)
    f.close()
    
