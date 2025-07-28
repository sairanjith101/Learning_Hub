# option 1
class Solution:
    def capitalize(self, s):
        return s.title()

s = "hello world from leetcode"
sol = Solution()
print(sol.capitalize(s))

# option 2
class Solution:
    def capital(self, s):
        result = []
        split_s = s.split()
        for word in split_s:
            result.append(word.capitalize())
        return ' '.join(result)

s = "hello world from leetcode"
sol = Solution()
print(sol.capital(s))