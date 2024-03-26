from typing import Dict, List, Tuple


def tuple_list_to_dict(my_list: List[Tuple[str, int]]) -> Dict[str, int]:
    result: Dict[str, int] = {}

    for key, value in my_list:
        if key not in result:
            result[key] = value

    return result


def intersect_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, Tuple[int, int]]:
    result: Dict[str, int] = {}

    for key, value in dict1.items():
        if key in dict2:
            result[key] = (value, dict2[key])

    return result


print(tuple_list_to_dict([('o', 2), ('t', 5), ('o', 7)]))
print(intersect_dicts({'o': 1, 'p': 2, 's': 5}, {'s': 2, 'p': 3, 't': 1}))



