def factorial(n):
    fakultaet = 1

    if n > 0:
        for i in range(1, n+1):
            fakultaet *= i
            print(str(fakultaet//i) + ' * ' + str(i) + ' = ' + str(fakultaet))
        return '\nEndergebnis: ' + str(fakultaet)

    elif n == 0:
        return 1

    else:
        return 'FactorialError'

print(factorial(6))

#Alt:
def factorial2(n):

    if n == 1 or n == 0:
        return 1

    else:
        return n*factorial2(n - 1)

print(factorial2(6))


