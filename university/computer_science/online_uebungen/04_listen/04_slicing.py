from typing import List


def even_indexes(my_list: List[int]) -> List[int]:
    return my_list[::2] #startet mit Wert 0!

    #Abwandlung für nur gerade Zahlen - kein Slicing allerings:
    '''liste_gerade: List[int] = []

    for i in my_list:
        if i % 2 == 0:
            liste_gerade.append(i)

    return liste_gerade'''


def reversed_special(my_list: List[int]) -> List[int]:
    return my_list[-2::-3] #- für Zählrichtung


def first_half(my_list: List[int]) -> List[int]:
    return my_list[:len(my_list)//2] #letzte Hälfte: my_list[len(my_list)//2+1:]


def rotate_right(my_list: List[int], count: int) -> List[int]:
    return my_list[-count:] + my_list[:-count]


print(even_indexes([3, 4, 6, 5, 2, 7, 9]))
print(reversed_special([3, 4, 6, 5, 2, 7, 9]))
print(first_half([3, 4, 6, 5, 2, 7, 9]))
print(rotate_right([1, 2, 3, 4, 5], 0), '-2->', rotate_right([1, 2, 3, 4, 5], 2))

#Erklärung rotate_right:
list1 = [1, 2, 3, 4, 5]
print(list1[-2:], list1[:-2])
print(rotate_right([1, 2, 3, 4, 5], 0), '-3->', rotate_right([1, 2, 3, 4, 5], 3))
print(list1[-3:], list1[:-3]) #Zählweise: Start 3.letztes Element; Cut: letzte 3

