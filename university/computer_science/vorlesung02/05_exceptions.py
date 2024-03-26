'''def div(x: float, y: float) -> float:
    if y == 0.0:
        raise Exception('You cannot divide by 0!')
    else:
        return x/y

print(div(5, 2))
#print(div(10,0))

print('**************************************')

print('Fangen von Exceptions:\n')

try:
    division = 5/0
except ZeroDivisionError:
    print('you divided by 0, didn\'t you?')

print(division)

print('***********************************')

def some_func(arg1: bool, arg2: int) -> int:
    if not arg1:
        raise ArgFalseException("Argument 1 was false!")
    if arg2 == 0:
        raise ArgZeroException("Argument 2 was zero!")
    return 1

try:
    some_func(False, 0)
except ArgFalseException:
    print('that did not work...')
except ArgZeroException:
    print('that did not work either...')

print('***********************************')'''

print('Fangen von Exceptions - Beispiel2:\n')

try:
    x = 5/0
except ZeroDivisionError:
    print('you divided by 0...')
finally:
    print('im Finally-Block')

try:
    x = 5/1
except ZeroDivisionError:
    print('you divided by 0...')
finally:
    print('im Finally-Block')



