Twenty = int()
Fifty = int()
Hundred = int()
TwoHundred = int()
FiveHundred = int()
TenHundred = int()
TwentyHundred = int()
while(True):
    dollar = int(input("Введите купюру "))
    if(dollar < 1):
        print (Twenty, Fifty, Hundred,TwoHundred, FiveHundred, TenHundred, TwentyHundred)
        break

    if(dollar == 200 or dollar == 500 or dollar == 1000 or dollar == 2000 or dollar == 5000 or dollar == 10000 or dollar == 20000 ):
        if(dollar == 200):
            Twenty = Twenty + dollar

        if(dollar == 500):
            Fifty = Fifty + dollar

        if(dollar == 1000):
            Hundred = Hundred + dollar

        if(dollar == 2000):
            TwoHundred = TwoHundred + dollar

        if(dollar == 5000):
            FiveHundred = FiveHundred + dollar

        if(dollar == 10000):
            TenHundred = TenHundred + dollar

        if(dollar == 20000):
            TwentyHundred = TwentyHundred + dollar

        
    else:
        print("Неправильная купюра")
        continue
        
    
    
