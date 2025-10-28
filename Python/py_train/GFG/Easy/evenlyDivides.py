class Solution:
    def evenlyDivides(self, n):
        count = 0
        for i in str(n):
            d = int(i)
            if d != 0 and n % d == 0:
                count += 1
        return count

n = 23
sol = Solution()
print(sol.evenlyDivides(n))