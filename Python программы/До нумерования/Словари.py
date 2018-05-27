Country = {}
Country = dict()
while (True):
    
    Names = input("Введите название страны ")
    Count = input("Введите численность ")
    Astana = input("Введите столицу ")
    S = input("Введите площадь ")
    Del = input("Введите что хотите удалить: ")
    if Del != ' ':
        del Country[Names]


    Country = {
        Names : {
            "Численность " : Count,
            "Столица " : Astana,
            "Площадь " : S,
            
        }
    }

    print(Country)
