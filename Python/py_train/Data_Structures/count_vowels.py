s = "Hello World"

class Solution:
    def countvowels(self, s):
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in s.lower():
            if i in vowels:
                count += 1
        return count

sol = Solution()
print(sol.countvowels(s))