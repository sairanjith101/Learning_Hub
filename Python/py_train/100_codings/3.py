class Solution:
    def vowels(self, str):
        vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        box = []
        for i in str:
            if i not in vowels:
                box.append(i)
        return ''.join(box)

str = "Python is Fun"
sol = Solution()
print(sol.vowels(str))