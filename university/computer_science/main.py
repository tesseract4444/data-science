# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def biggest(a: int, b: int, c: int) -> int:
    current_biggest: int = a

    if b > a:
        current_biggest = b

    if c > current_biggest:
        current_biggest = c

    return current_biggest

    #max_value = max(a, b, c)
    #return max_value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(biggest(2,4,3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
