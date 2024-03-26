def ggt(first, second):
    if first == 0:
        print(second)
    else:
        while second != 0:
            if first > second:
                first = first - second  # zahl2 wird solange abgezogen von zahl1 bis 0
            else:
                second = second - first
    print("The biggest common divisor is " + str(first))


ggt(25, 5)
