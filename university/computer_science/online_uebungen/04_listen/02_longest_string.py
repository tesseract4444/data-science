from typing import List, Optional


def longest_string(my_list: List[str]) -> Optional[str]:
    if len(my_list) == 0:
        return None
    else:
        return max(my_list, key=len) + ': ' + str(len(max(my_list, key=len)))

print(longest_string(['hallo', 'duschlampe', 'Winter']))
print(longest_string([]))


#Alternative:
from typing import List, Optional


def longest_string(my_list: List[str]) -> Optional[str]:
    longest: Optional[str] = None

    for string in my_list:
        if longest is None or len(string) > len(longest):
            longest = string

    return longest