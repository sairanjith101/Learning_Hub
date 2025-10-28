class Solution:
    def isPowerofTwo(self, n):
        # code here
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

n = 8
sol = Solution()
print(sol.isPowerofTwo(n))