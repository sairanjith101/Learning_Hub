class Solution:
    def temp(self, a, b):
        a = a + b
        b = a - b
        a = a - b
        return a, b

sol = Solution()
print(sol.temp(5, 10)) 