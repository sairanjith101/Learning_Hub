n = int(input("Enter a value: "))

class Solution:
    def fibonaccinum(self, n):
        output = []
        a,b = 0,1
        for i in range(n):
            output.append(a)
            a,b = b, a+b
        return output

sol = Solution()
print(sol.fibonaccinum(n))