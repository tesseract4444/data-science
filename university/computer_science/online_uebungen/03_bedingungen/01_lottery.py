import random

def calculate_lottery_win(pot: float, win_class: int) -> float:
    if win_class == 1:
        return pot*0.001
    elif win_class == 2:
        return pot*0.005
    elif win_class == 3:
        return pot*0.02
    elif win_class == 4:
        return pot*0.125
    elif win_class == 5:
        return pot*0.5
    else:
        return 0

print(f'{calculate_lottery_win(20000, random.randint(1, 5))} $')