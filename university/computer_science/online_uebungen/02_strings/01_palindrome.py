def is_palindrome(word: str) -> bool:
    lower: str = input('Bitte Wort zur Palindrom-Prüfung eingeben...\n').lower()

    for i in range (len(lower)//2):
        if lower[i] != lower[-i-1]:
            return False
    return True

print(is_palindrome(''))