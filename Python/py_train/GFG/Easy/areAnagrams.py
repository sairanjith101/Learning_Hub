class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       return sorted(s1) == sorted(s2)

s1 = "listen"
s2 = "lists" 
sol = Solution()
print(sol.areAnagrams(s1, s2))