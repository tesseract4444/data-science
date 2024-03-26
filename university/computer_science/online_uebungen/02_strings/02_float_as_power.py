from math import log10

def format_floating_point_exponential(number: float) -> str:
    number = float(input())
    exponent: int = int(log10(number)) #int rundet ab, damit bleibt log10 korrekt!
    new_num = str(number / (10 ** exponent))
    return '{}e{}'.format(new_num, exponent)

print(format_floating_point_exponential(''))


