def main():
    print("Введи своих друзей ")
    friends1 = list(friends_one())
    print("введите друзей соседа ")
    friends2 = list(friends_one())
    print("Твои друзья ", friends1)
    print("Друзья соседа ", friends2)
    print("Возможные друзья ", possible_friends(friends1,friends2))
    print("Сосед может познакомиться с ", possible_friends(friends2 , friends1))
    print("Общие друзья ", mutual_friends(friends1, friends2))
def possible_friends(a , b):
    return set(a) - set(b)

def mutual_friends(a , b):
    return set(a) & set(b)

def friends_one():
    friend = []
    a = int(input("введите количество друзей "))
    for i in range (0 , a):
        b = input()
        friend.append(b)
    return friend
