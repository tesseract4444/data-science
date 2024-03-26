from typing import List, Optional


def average(my_list: List[int]) -> Optional[float]:
    #length: int = len(my_list)

    if len(my_list) == 0: #bzw. 'if length == 0'
        return None

    sum = 0

    for i in my_list:
        sum += i

    return sum/len(my_list) #entspricht #length oben

print(average([1, 3, 6, 12]))