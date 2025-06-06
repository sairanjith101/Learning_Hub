s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution:
    def reverse_string(self, s):
        return s[::-1]

sol = Solution()
print(sol.reverse_string(s))