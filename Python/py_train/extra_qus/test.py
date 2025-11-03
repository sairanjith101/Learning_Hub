class Solution:
    def fibonacci_series(self, n):
        output = []
        a,b = 0,1
        for i in range(n):
            output.append(a)
            a,b = b, a+b
        return output

n = int(input("Enter a value: "))
sol = Solution()
print(sol.fibonacci_series(n))