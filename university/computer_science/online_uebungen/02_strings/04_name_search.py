from typing import Tuple, List

def name_search(all_names: List[str], fragment: str) -> List[Tuple[str, str]]:
    all_names: List[str] = \
        {
        'anna', 'otto', 'jack', 'lena', 'tom', 'arthur', 'laura', 'james', 'lili', 'chris', 'neil', 'alex', 'michael',
        'john', 'helena', 'zoe', 'robert', 'lisa', 'joanne', 'julian', 'felix', 'sophie', 'lara', 'jonathan'
    }

    result: List[Tuple[str, str]] = []

    for name in all_names:
        if fragment in name:
            index: int = name.index(fragment)
            result.append((name[:index], name[index + len(fragment):]))

    return result


print(name_search('', 'en'))


'''
def name_search(all_names: List[str], fragment: str) -> List[Tuple[str, str]]:

    result: List[Tuple[str, str]] = []

    for name in all_names:
        if fragment in name:
            index: int = name.index(fragment)
            result.append((name[:index], name[index + len(fragment):]))

    return result


all_names: List[str] = \
{
        'anna', 'otto', 'jack', 'lena', 'tom', 'arthur', 'laura', 'james', 'lili', 'chris', 'neil', 'alex', 'michael',
        'john', 'helena', 'zoe', 'robert', 'lisa', 'joanne', 'julian', 'felix', 'sophie', 'lara', 'jonathan'
    }

print(name_search(all_names, 'en'))'''
