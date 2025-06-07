a = 5
b = 10  
# Output: a = 10, b = 5

class Solution:
    def swapwithouttemp(self, a, b):
        a = a + b
        b = a - b
        a = a - b
        return [a, b]

sol = Solution()
print(sol.swapwithouttemp(a,b))