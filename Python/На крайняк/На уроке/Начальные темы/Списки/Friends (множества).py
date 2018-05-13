def main():
    print('Введи своих друзей')
    friends1 = list(friends_one())
    print('Введи друзей соседа')
    friends2 = list(friends_one())
    print('Твои друзья', friends1)
    print ('Друзья соседа:',friends2)
    print('Возможные друзья',possible_friends(friends1,friends2))
    print('Сосед может познакомиться с',possible_friends(friends2,friends1))
    print('Общие друзья',mutual_friends(friends1,friends2))

def friends_one():
    spis = []
    kol = int(input('Введите кол-во друзей'))
    for i in range(kol):
        drug = input('Введите друга')
        spis.append(drug)
    return spis

def possible_friends(x,y):
    a = set(y) - set(x)
    return (a)
    
def mutual_friends(x,y):
    b = set(x) & set(y)
    return(b)
    



    
main()
