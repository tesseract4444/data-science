from typing import List


def filter_greater(vector: List[int], x: int) -> List[int]:
    filtered: List[int] = []

    for i in vector:
        if i > x:
            filtered.append(i)

    return filtered


def count_lower(vector: List[int], x: int) -> int:
    count: int = 0

    for i in vector:
        if i < x:
            count += 1

    return count



def bank_card_security_value(digits: List[int]) -> int:
    security_value: int = 0

    for (index, element) in enumerate(digits):
        security_value += (index + 1) * element #1.Zahl mit index0: 0+1 usw.

    return security_value


def vector_length(vector: List[int]) -> float:
    sum = 0

    for i in vector:
        sum += i * i

    return sum ** 0.5


def vector_add_scalar(vector: List[int], scalar: int) -> List[int]:
    new_vector: List[int] = []

    for i in vector:
        new_vector.append(i + scalar)

    return new_vector


def vector_add_vector(vector1: List[int], vector2: List[int]) -> List[int]:
    if len(vector1) != len(vector2):
        return []

    vector3: List[int] = []

    for i in range(len(vector1)):  # len(vector2) auch möglich, da in diesem Fall beide sowieso gleichlang
        vector3.append(vector1[i] + vector2[i])  # addiere 1.Element von v1 mit 1.Element von v2 usw.

    return vector3


def flatten_lists(list_of_lists: List[List[int]]) -> List[int]:
    flat_list: List[int] = []

    for inner_list in list_of_lists:
        flat_list += inner_list #fügt komplette Liste hinzu

    #Oder: jedes Element einzeln hinzugefügt
        #for element in inner_list:
            #flat_list.append(element)

    return flat_list

print(filter_greater([16, 12, 7, 11], 11))
print(count_lower([i for i in range(5)], 7)) #0-4 => 5
print(bank_card_security_value([i for i in range(6)])) #als Ergebnis nur ein Wert = Sicherheitswert
print(vector_length([4, 3]))
print(vector_add_scalar([-5, 6, -12], 8))
print(vector_add_vector([-5, 6, -8], [5, 4, 8]))
print(flatten_lists([[3, 4], [7], [8, 11, 5], [6, 6]])) #List of List: [[]]

print('***********************************************')

#exkurs enum()
names_list = ['Anna', 'Thea', 'Olga', 'Nina']
#names_all = enumerate(names_list)

for i in enumerate(names_list):
    print(i)

for i, j in enumerate(names_list):
    print(i, j)

