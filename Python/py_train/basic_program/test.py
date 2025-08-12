class Solution:
    def swap(self, a, b):
        a = a + b
        b = a - b
        a = a - b
        return a, b

a = 5
b = 10
sol = Solution()
print(sol.swap(a, b))