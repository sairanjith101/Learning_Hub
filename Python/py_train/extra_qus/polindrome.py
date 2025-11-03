def is_palindrome(word: str) -> bool:
    reverse_word = word[::-1]
    if reverse_word == word:
        return "True"
    return "False"


word = "madam"

print(is_palindrome(word))