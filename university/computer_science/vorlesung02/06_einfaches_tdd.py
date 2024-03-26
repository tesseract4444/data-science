def test(i):
    if i == 0:
        return 'Fehler'
    return 5 / i #ändern andere Zahl als 5: Fehler!!!

assert (test(0) == 'Fehler')
assert (test(1) == 5)
assert (test(2) == 2.5)

print('************************************')

from typing import List

def list_contains(l: List[int], x: int) -> bool:
    for y in l:
        if x == y:
            return True

    return False

assert(list_contains([], 0) == False)
assert(list_contains([0], 0) == True)
assert(list_contains([i for i in range(10)], 9) == True)

print('************************************')
print('Aufgabe zu TDD:\n')
from typing import List

def get_index(numbers: List[int], x:int) -> int:
    index = 0
    for i in numbers:
        if i == x:
            return index
        index += 1
    return -1

assert(get_index([], 2) == -1)
assert(get_index([1], 2) == -1)
assert(get_index([1, 2], 2) == 1)
assert(get_index([0, 2, 4, 6, 8], 0) == 0)
assert(get_index([-10, -5, 0, 5, 10, 10], 10) == 4)