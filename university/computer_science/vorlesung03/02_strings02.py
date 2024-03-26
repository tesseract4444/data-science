my_str: str = 'Hallo!'
print('Länge des Wortes Hallo: ', len(my_str))

#Iteration
for char in my_str:
    print(char)

print(my_str + 'Hey!')
print(my_str * 2)
print('H' in my_str)
print('i' in my_str)
print(my_str[0] + '::' + my_str[1:])
print(my_str[::-1])

print('********************************************')

from typing import List

my_string: str = '1, 2, 3, 4, 5, 6, 7, 8, 9'
my_part_string: List[str] = my_string.split(', ')
print(my_part_string)
my_other_string: str = '-'.join(my_part_string)
print(my_other_string)

print('********************************************')

def is_palindrome(word:str) -> bool:
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            return False
        return True

assert(is_palindrome('otto') is True)
assert(is_palindrome('max') is False)
assert(is_palindrome('lagerregal') is True)

#print('********************************************')

print('Formatter:')

name = 'Testsubjekt'
value = 5
print('Spieler {} hat {} Punkte erzielt.'.format(name, value))

print('********************************************')

print('Beispiele - Formatter:')

s1 = 'x = {}, y = {}, z = {}'.format(11, 22, 33)
print(s1)

s2 = 'x = {2}, y = {1}, z = {0}'.format(11, 22, 33)
print(s2)

s3 = 'x = {fir}, y = {thi}, z = {sec}'.format(fir=11, sec=22, thi=33)
print(s3)

print('********************************************')

from typing import Dict

x: int = 3
squares_dict: Dict[int, int] = {i: i * i for i in range(x)}

print(f'Die Quadrate der ersten {x} Zahlen sind: {squares_dict}')

print('********************************************')

my_str: str = 'Dies ist ein Test.'

my_str_upper: str = my_str.upper()
print(my_str_upper)

my_str_lower: str = my_str.lower()
print(my_str_lower)

my_str_replaced = my_str.replace('i', 'o')
print(my_str_replaced)
