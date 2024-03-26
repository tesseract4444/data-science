def func():
    print('Dies hier ist eine Funktion')
    print('Auch dies ist eine Funktion')

func()

print('**************************************')


def test():
    print("Ausgeführt!")
    return True

    print('Nicht ausgeführt!')

print(test())

print('**************************************')


def my_first_func():
    print(1234)
x = my_first_func()
print(x)  # Funktion macht keinen Return, also None
print()


def my_second_func():
    return 1234
y = my_second_func()
print(y)

print('**************************************')


# Funktionsargumente
def ausgabe(print1, print2, print3):
    if print1:
        print("1. Statement")
    if print2:
        print("2. Statement")
    if print3:
        return #gibt nichts mehr aus wegen "return" mit "print"
        print("3. Statement")
ausgabe(True, False, True)

print('**************************************')

print('Funktionen und Type hints:')


def my_func(arg1: bool, arg2: int, arg3: str) -> int:
    if arg1:
        return -1
    elif arg3 == 'test':
        return arg2
    else:
        return 0
print(my_func(False, 42, 'test'))

print('**************************************')

print('Parabelgleichung:')

def parabel(a: float, b: float, c: float, x: float) -> float:
    return a * x * x + b * x + c
print(parabel(3, 5, 3, 6))


def is_in_interval(x: int, a: int, b: int) -> bool:
    return a <= x and x <= b
print(is_in_interval(8, 4, 9))

print('**************************************')
import math

def nullstellen(a: float, b: float, c: float) -> float:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2

print(nullstellen(-4, 4, 3))

print('**************************************')

def greet(who: str, greetings: str = 'Hello, ') -> str:
    print(greetings + who)

greet('Simon!', 'Good to see you, ')
greet('Hannah!')

print('**************************************')

def func_1():
    print('A')
a = func_1()

def func_2():
    return 'B'
b = func_2()
print(b)

def func_3(arg1: bool, arg2: str):
    if arg1 == False:
        return 0
    elif arg2 == 'test':
        return 2
    else:
        return 4
print(func_3(True, 'tesst'))

print('**************************************')

def biggest(a, b, c):
    current_biggest = a
    if b > a:
        current_biggest = b
    if c > current_biggest:
        current_biggest = c
    return current_biggest

print(biggest(4, 2, 8))


def alt_biggest(a, b, c):
    return max(a, b, c)

print(alt_biggest(4, 2, 8))
