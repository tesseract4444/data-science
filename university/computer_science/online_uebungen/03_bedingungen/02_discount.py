def calculate_discount(price: float, has_dog: bool, has_cat: bool, has_hamster: bool) -> float:
    if has_dog and has_cat:
        price -= 0.08 * price
    elif has_dog:  # and not has_cat
        price -= 0.05 * price
    elif has_cat:  # and not has_dog
        price -= 0.05 * price
    else:  # not has_dog and not has_cat
        price

    if has_hamster:
        return price - 0.02 * price
    else:
        return price

print(round(calculate_discount(10.00, True, True, True), 2))


'''def calculate_discount(price: float, has_dog: bool, has_cat: bool, has_hamster: bool) -> float:
    if has_dog and has_cat:
        return price - 0.05 * price


    elif has_dog or has_cat:
        return price - 0.08 * price

    elif (has_dog or has_cat) and has_hamster:
        return price - (0.05+0.02) * price

    elif has_hamster and (has_dog and has_cat):
        return price - (0.08+0.02) * price

    elif has_hamster:
        return price - 0.02 * price



print(calculate_discount(10.00, True, True, True))'''
