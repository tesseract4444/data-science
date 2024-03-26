from typing import Tuple, List

def min_max(my_list: List[int]) -> Tuple[int, int]:
    list_min = my_list[0]
    list_max = my_list[0]

    for x in my_list:
        if x < list_min:
            list_min = x
        elif x > list_max:
            list_max = x

    return list_min, list_max



def account_value(stocks: List[Tuple[str, int]]) -> float:
    price_sum = 0.0
    for name, price in stocks:
        price_sum += price

    return price_sum


def stock_value(stocks: List[Tuple[str, int]], name: str) -> int:
    for stock_name, price in stocks:
        if stock_name == name:
            return price #name, price
    return -1


print(min_max([5*12, 6*13, 9*11]))

stock_values_1: List[Tuple[str, int]] = [
        ("iag", 100.00), ("dag", 120.00)
    ]
stock_values_2: List[Tuple[str, int]] = [
        ("eag", 87.99), ("sag", 117.52)]

print(account_value(stock_values_1 + stock_values_2))
print(stock_value(stock_values_1, 'dag'))