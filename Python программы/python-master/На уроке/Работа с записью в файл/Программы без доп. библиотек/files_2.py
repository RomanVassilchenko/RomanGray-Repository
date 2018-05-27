
chis_1 = int(input('Введите первое число: '))
znak = input('Введите знак')
chis_2 = int(input('Введите первое число'))
if znak == '+':
    eq = chis_1 + chis_2
if znak == ' -':
    eq = chis_1 - chis_2
if znak == '*':
    eq = chis_1 * chis_2
if znak == '*':
    eq = chis_1 * chis_2
summ = str(chis_1) + znak + str(chis_2)+ '='+str(eq)
with open('test.txt','r+') as f:

    f.write(summ)
    f.close()

print(summ)

