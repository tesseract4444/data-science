from datetime import datetime #datetime eigentlich nicht Teil der Aufgabenstellung

def greet(hour: int) -> str:
        if 0 <= hour < 6:
            return "Gute Nacht!"
        elif 6 <= hour < 12:
            return "Guten Morgen!"
        elif 12 <= hour < 18:
            return "Guten Tag!"
        elif 18 <= hour < 22:
            return "Guten Abend!"
        elif 22 <= hour <= 24:
            return "Gute Nacht!"
        else:
            return "Ich weiß die Zeit grad net :(."

def minute_format():
    if datetime.now().minute < 10:
        return '0'
    else:
        return ''

#print(greet(88))
#print(greet(datetime.now().hour))
print(f'Es ist {datetime.now().hour}:{minute_format()}{datetime.now().minute} Uhr. {greet(datetime.now().hour)}')