class Solution:
    def FrequencyofChar(self, str):
        char = {}
        for i in  str:
            if i not in char:
                char[i] = 1
            else:
                char[i] += 1
        return char
            

str = "Python 3"
sol = Solution()
print(sol.FrequencyofChar(str))