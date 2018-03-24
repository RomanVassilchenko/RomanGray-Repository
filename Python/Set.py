PDD = {"Henri", "Adolf", "Ruzveld"}
Nalogi = {"Катя" , "Henri", "Roman", "Nikita"}
All = PDD.intersection(Nalogi)
print("Нарушили правила и не заплатили:", All)
AllNalogi = Nalogi.difference(PDD)
print("Не платили , но не нарушали:" , AllNalogi)
