class Solution:
    def First_Non_Repeating_Char(self, s):
        char_index = {}

        # Step 1: Count each character
        for char in s:
            if char not in char_index:
                char_index[char] = 1
            else:
                char_index[char] += 1

        # Step 2: Check for first non-repeating character
        for char in s:
            if char_index[char] == 1:
                return char

        return -1  # If all characters are repeating

# Example usage
s = "leetcode"
# s = "aabbcddde"
sol = Solution()
print(sol.First_Non_Repeating_Char(s))  # Output: 'l'
