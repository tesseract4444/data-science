from typing import Dict, List


def count_char_occurrences(my_str: str) -> Dict[str, int]:
    my_str = my_str.lower()
    result: Dict[str, int] = {}
    count = 0

    for char in my_str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


def word_position_list(my_str: str) -> Dict[str, List[int]]:
    result: Dict[str, List[int]] = {}

    if len(my_str) == 0:
        return result

    for index, word in enumerate(my_str.split(' ')):
        if word in result:
            result[word].append(index)
        else:
            result[word] = [index]

    return result


def merge_dicts_with_add(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    result: Dict[str, int] = {}

    for key, value in dict1.items():
        result[key] = value

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result

print(count_char_occurrences('Hello'))
print(word_position_list('dies ist ein test'))
print(word_position_list(''))
print(merge_dicts_with_add({'o': 7, 't': 2, 's': 5}, {'o':1, 's':2}))