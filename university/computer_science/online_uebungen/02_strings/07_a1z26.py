from typing import List

ord_a: int = ord('a') #ord() Funktion gibt Unicode von Buchstabe aus


def encrypt_letter(letter: str) -> int:
    return ord(letter) - ord_a + 1


def decrypt_letter(letter: int) -> str:
    return chr(ord_a + letter - 1) #zeigt Buchstabe aus eingegebenem Unicode an


def encrypt_word(word: str) -> List[int]:
    result: List[int] = []

    for letter in word:
        result.append(encrypt_letter(letter))

    return result

def decrypt_word(word: List[int]) -> str:
    result: str = ''

    for letter in word:
        result += decrypt_letter(letter)

    return result

print(ord('a'))
print(encrypt_letter('d'))
print(decrypt_letter(25))
print(encrypt_word('test'))
print(decrypt_word([8, 1, 12, 12, 15]))


