class Solution:
    def anagrams(self, s, t):
        return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.anagrams(s,t))