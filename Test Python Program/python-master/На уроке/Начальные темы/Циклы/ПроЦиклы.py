chis1 = input("Первое число: ")
if chis1 == "0" or chis1 =="":
   
    while chis1=="" or chis1=="0":
        print("Error")
        chis1 = input("Первое число: ")
        
        
while True:
    chis2 = input("Число2: ")
    if chis2 == 0 or chis2 =="":
        print("Error")
        continue
    chis1 = int(chis1)
    chis2 = int(chis2)
    
    chis1 += chis2

    
    print("Sum: ",chis1)
           
