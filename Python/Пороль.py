import re
a = input()
chislo = int(0)
bukva = int(0)
znak = int(0)
if(len(a) < 8):
    print("Error")
else:
    a.lower()
    for i in range(0 , len(a)):
        if(a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9' or a[i] == '0'):
             chislo = chislo + 1
        if(a[i] == ')' or a[i] == '(' or a[i] == '*' or a[i] == '&' or a[i] == '^' or a[i] == '%' or a[i] == '$' or a[i] == '#' or a[i] == '@' or a[i] == '!' or a[i] == "[" or a[i] == '}' or a[i] == ',' or a[i] == '.' or a[i] == '|' or a[i] == '/'   ):
            znak = znak + 1
        if(a[i] == 'm' or a[i] == 'n' or a[i] == 'b' or a[i] == 'v' or a[i] == 'c' or a[i] == 'x' or a[i] == 'z' or a[i] == 'l' or a[i] == 'k' or a[i] == 'j' or a[i] == 'h' or a[i] == 'g' or a[i] == 'f' or a[i] == 'd' or a[i] == 's' or a[i] == 'a' or a[i] == 'p' or a[i] == 'o' or a[i] == 'i' or a[i] == 'u' or a[i] == 'y' or a[i] == 't' or a[i] == 'r' or a[i] == 'e' or a[i] == 'w' or a[i] == 'q' ):
            bukva = bukva + 1

if(bukva > 1 & znak > 1 & chislo > 1):
    print("Круто")
else:
    print("Не круто")
