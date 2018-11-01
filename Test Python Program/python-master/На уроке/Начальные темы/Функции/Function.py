
def main():
    sum1 = 0
    count = int (input("Количество банкнот"))
    for i in range(1,count+1):
       
        money = int(input("Купюра"))
        while proverka(money)!=True:
            money = int(input("Введите банкноту"))
        sum1 += money
        
            
    result(sum1)
 

def proverka(money):
    if money ==200 or money==500 or money==1000 or money==2000 or money==5000 or money==10000 or money==20000:
        return True
    else:
        
        print("введите еще раз")
        return False     
def result(summa):
    print(summa)



main()






    
           
        
