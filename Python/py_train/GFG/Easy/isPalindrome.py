class Solution:
    def isPalindrome(self, s):
        # code here
        return s == s[::-1]

s = "abc" 
sol = Solution()
print(sol.isPalindrome(s))