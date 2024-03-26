def fibonacci(number: int) -> int:

    if not isinstance(number, int):
        raise Exception('Es muss sich hier um eine Ganzzahl handeln!')

    if number < 0:
        raise Exception('Die Zahl muss größer sein als 0!')

    if number == 0 or number == 1:
        return 1

    return fibonacci(number-1) + fibonacci(number-2)


print(fibonacci(5))
'''
fib(5) = fib(5-1) + fib(5-2) = 5 + 3 = 8   
'''

print(fibonacci(6))
'''
fib(6) = fib(6-1) + fib(6-2) = 8 + 5 = 13
'''

'''Erklärung: fibonacci() zählt die jeweiligen 
Ergebnisse der zuvor berechneten Zahlen immer weiter hoch, 
angefangen mit 0(Stelle0) und 1(Stelle1)
'''