def ggt(a, b):

    #a = int(input())
    #b = int(input())
    divisor = 1 #nicht unbedingt nötig
    minimum = min(a, b) #kleinster Wert ist immer der größtmögliche Teiler

    for i in range(1, minimum + 1): #minimum+1 da Grenzwert normal -1 bei range()
        if (a % i == 0) and (b % i == 0):
            divisor = i

    return divisor

print(ggt(3, 9))


assert(ggt(12, 4) == 4)
assert(ggt(3, 7) == 1)
assert(ggt(46, 64) == 2)
assert(ggt(777, 111) == 111)
assert(ggt(15, 25) == 5)
assert(ggt(30, 60) == 30)
