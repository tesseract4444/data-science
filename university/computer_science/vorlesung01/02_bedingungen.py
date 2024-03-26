client_has_dog = True
if client_has_dog:
    print("20% auf Hundefutter!")
else:
    print("Kauf dir erst \'nen Hund!\n")


dice_value = 5
if dice_value == 6:
    print("Sechs gewürfel!")
else:
    print("Keine Sechs gewürfelt!")


if dice_value == 1:
    print("Eins!")
else:
    if dice_value == 2:
        print("Zwei!")
    else:
        if dice_value == 3:
            print("Drei!")


if dice_value == 1:
    print("Eins gewürfelt!")
elif dice_value == 2:
    print("Zwei gewürfelt!")
elif dice_value == 3:
    print("Drei gewürfelt!")
elif dice_value == 4:
    print("Vier gewürfelt!")
elif dice_value == 5:
    print("Fünf gewürfelt!")
else:
    #dice_value == 6:
    print("Sechs gewürfelt!")


value = 1
if value > 0:
    print("Positiv")

value = -1
if value > 0:
    print("Positiv")
elif value < 0:
    print("Negativ")
else:
    print("Null")


print('\n\nHausaufgabe zu Bedingungen:\n')
value = int(input("Bitte negative Zahl, positive Zahl eingeben, 0 auch erlaubt..."))
if value < 0:
    print('Negativ')
elif value > 0:
    print('Positiv')
else:
    print('Null')

print()

punkte0 = int(input('Bitte nur 100, 80, 50 oder 0 einsetzen...'))
if punkte0 >= 80:
    print("Gut gemacht!")

punkte = int(input('Bitte hier die erreichten Punkte einsetzen...'))
if 90 < punkte <= 100:
    print(1)
elif punkte > 80:
    print(2)
elif punkte > 70:
    print(3)
elif punkte > 60:
    print(4)
elif punkte > 50:
    print(5)
elif punkte <= 50:
    print(6)

print('***********************************************************')
while True:
    a = int(input('Bitte Zahl zwischen 1 und 6 eingeben...'))
    if a == 4:
        print("Sieger!!!")
        break
    elif a > 0 and a < 7 and a != 4:
        print("Pech, musst leider weiterraten!")
        #a = int(input('Bitte Zahl zwischen 1 und 6 eingeben...'))
    elif a <= 0 or a > 6:
        print("Bitte NUR eine ZAHL zwischen 1 und 6 eingeben, verdammt nochmal!!!")
        #a = int(input('Bitte Zahl zwischen 1 und 6 eingeben...'))


