class Solution:
    def code_stub(self, n):
        box = []
        for i in range(1, n+1):
            box.append(str(i))
        return ''.join(box)

n = int(input("Enter a value: "))
sol = Solution()
print(sol.code_stub(n))