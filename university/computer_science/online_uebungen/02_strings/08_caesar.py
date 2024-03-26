from typing import Optional

class CaesarCipher:
    point_a = ord("a")

    def __init__(self, rounds: int):
        self.rounds: int = rounds

    def crypt_letter(self, lower_letter: str) -> str:
        point: int = ord(lower_letter) - self.point_a
        new_point: int = (point + self.rounds) % 26
        return chr(new_point + self.point_a)

    def decrypt_letter(self, lower_letter: str) -> str:
        point: int = ord(lower_letter) - self.point_a
        new_point: int = (point - self.rounds) % 26
        return chr(new_point + self.point_a)

    def crypt_word(self, lower_word: str) -> str:
        return ''.join(map(self.crypt_letter, lower_word))

    def decrypt_word(self, lower_word: str) -> str:
        return ''.join(map(self.decrypt_letter, lower_word))

    def crypt_text(self, text_lower: str) -> str:
        encrypted_sentences: List[str] = []

        for sentence in text_lower.split('.'):
            encrypted_sentences.append(' '.join(map(self.crypt_word, sentence.split(' '))))

        return '.'.join(encrypted_sentences)

    def decrypt_text(self, text_lower: str) -> str:
        decrypted_sentences: List[str] = []

        for sentence in text_lower.split('.'):
            decrypted_sentences.append(' '.join(map(self.decrypt_word, sentence.split(' '))))

        return '.'.join(decrypted_sentences)


word_list = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie", "der", "die", "das"]


def crack_caesar(encrypted_text: str) -> Optional[str]:
    for possible_rounds in range(1, 26):
        caesar_cipher = CaesarCipher(possible_rounds)
        decrypted = caesar_cipher.decrypt_text(encrypted_text)

        for start_word in word_list:
            if decrypted.startswith(start_word + ' '):
                return decrypted

    return None

caesar_three = CaesarCipher(3)
caesar_symmetric = CaesarCipher(13)

print(caesar_three.crypt_letter('a'))
print(caesar_three.decrypt_letter('d'))
print(caesar_three.crypt_word('python'))
print(caesar_three.crypt_text('Hallo Welt.'))
print(caesar_symmetric.crypt_text("qnf xanpxra qre prnfne puvsser vfg rvaqrhgvt mh rvasnpu"))
print(crack_caesar("zpl ohilu klu jvkl nlruhjra"))