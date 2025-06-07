n = int(input("Enter a value: "))

class Solution:
    def primenum(self, n):
        if n <= 1:
            return 'Number must be above 1'
        for i in range(2, n):
            if n % i == 0:
                return "Not Prime Number"
        else:
            return "Prime Number"

sol = Solution()
print(sol.primenum(n))
