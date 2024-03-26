from typing import List

my_list: List = [0, 'eins', 2 / 1, 2 * 1.5, 2 ** 2]
#my_list[index]
#my_list[start_index:end_index]
#my_list[start_index:end_index:schrittweise]

print('********************************************')

from typing import Tuple

my_tuple: Tuple[int, int, int] = (1, 2, 3)
print('tupel: ', my_tuple)
first_elem: int = my_tuple[0]
print('first element: ', first_elem)

new_tuple: Tuple[int, int] = my_tuple[:2]
print('neues tupel: ', new_tuple)
other_new_tuple: Tuple[int, int] = my_tuple[::2]
print('noch so ein tupel: ', other_new_tuple)

concatenated_tuple: Tuple[int, int, int, int, int, int] = my_tuple * 2
print('concatenation: ', concatenated_tuple)

#del my_tuple[0] #geht nicht, da tupel keine item-zuweisung unterstützt!
#my_tuple[1] = 3

print('********************************************')

print('dictionaries\n')

from typing import Dict, Any

persDic: Dict[str, Any] = {'alter': 50, 'groesse': 170, 'nation': 'deutsch'}

print(persDic['alter'], ';', persDic['groesse'])
print(persDic['nation'])

#Update eines Wertes
persDic['alter'] = 51
print(persDic['alter'])

#Hinzufügen eines Schlüssel-Wert-Paares
persDic['geschlecht'] = 'weiblich'
print(persDic['geschlecht'])

print('********************************************')

from typing import Dict

values: Dict[int, str] = {1: 'rot', 2: 'blau', 3: 'rot'}
for (key, value) in values.items():
    print("{} -> {}".format(key, value))

print('********************************************')

from typing import List, Dict

def count_frequency(nums: List[int]) -> Dict[int, int]:
    counts = {}

    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    return counts

assert({} == count_frequency([]))
assert({1: 3} == count_frequency([1, 1, 1]))
assert({1: 3, 2: 4} == count_frequency([1, 2, 2, 1, 2, 1, 2]))

print('********************************************')

