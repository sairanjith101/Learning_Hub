from typing import List, Tuple

class Solution:
    def findnum(self, vowels: List[str], spaces: List[str], user: str) -> Tuple[int, int, int]:
        vowels_count = 0
        spaces_count = 0
        consonants_count = 0  # Fixed spelling

        for i in user.lower().strip():  # Convert to lowercase
            if i in vowels:  # Check if the character is in the vowels list
                vowels_count += 1
            elif i in spaces:  # Check if the character is in the spaces list
                spaces_count += 1
            elif i.isalpha():  # Check if the character is a consonant
                consonants_count += 1

        return vowels_count, consonants_count, spaces_count  # Return as a tuple

# Input
vowels = ['a', 'e', 'i', 'o', 'u']
spaces = [' ']
user = input("Enter the value: ")

sol = Solution()
print(sol.findnum(vowels, spaces, user))
