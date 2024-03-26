from typing import Tuple

'''def file_name_and_ending(filename: str) -> Tuple[str, str]:
    contents = filename.split('.')
    if len(contents) == 1: #Dateien ohne Endung
        return contents[0], ''
    elif contents[0] == '': #Normale Dateien
        return contents[1]
    else: #Dateien mit mehr als einer Endung
        return '.'.join(contents[:-1]), contents[-1]

print(file_name_and_ending('hackbot'))
print(file_name_and_ending('hackbot.exe'))
print(file_name_and_ending('hackbot.conf.exe.json'))'''

#myAlt:
def file_name_and_ending(filename: str) -> Tuple[str, str]:
    contents = filename.split('.')
    if len(contents) == 1: #Dateien ohne Endung
        return contents[0], ''
    elif len(contents) == 2: #Normale Dateien
        return contents[0], contents[1]
    elif len(contents) > 2: #Dateien mit mehr als einer Endung
        return '.'.join(contents[0:-1]), contents[-1]

print(file_name_and_ending('hackbot'))
print(file_name_and_ending('hackbot.exe'))
print(file_name_and_ending('hackbot.conf.exe.json'))

