iq = 10


while iq > 0 :
    time = int (input ("Сейчас времени:"))
    if time >=6 and time <12:
       print("сейчас утро")
    elif time == 12:
       print("сейчас полдень")
    elif time >12 and time <=18:
       print("сейчас обед")
    elif time >18 and time <23:
       print("сейчас вечер")
    elif time == 24:
       print("сейчас полночь")
    elif time >=1 and time <6:
       print("сейчас ночь")
    if time >24:
        print("Похоже у тебя в сутках больше 24 часов")

