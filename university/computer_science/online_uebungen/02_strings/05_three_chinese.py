def three_chinese(line: str, target_vowel: str) -> str:
    replace_vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü']
    result: str = line

    for char in replace_vowel:
        result = result.replace(char, target_vowel)

    result = result.replace(target_vowel + target_vowel, target_vowel)

    return result

print(three_chinese('Drei Chinesen mit nem Kontrabass.', 'ü'))

