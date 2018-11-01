def Name ():
    T = int(0)
    AllName = ["Катя", "Никита", "Роман"]
    while(True):
        Names = input("Введите имя ")
        for i in range (0, len(Names)):
            if(Names[i] == ","):
                AllName.insert(len(Names),Names)
                T = T + 1
        if(T == 0):
            AllName.append(Names)
        T = 0
        print(AllName)
Name()
