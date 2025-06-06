s = "A man, a plan, a canal: Panama"
# Output: True
s = "race a car"
# Output: False

class Solution:
    def Palindrome(self, s):
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        cleaned_str = ''.join(cleaned)
        return cleaned_str == cleaned_str[::-1]

sol = Solution()
print(sol.Palindrome(s))