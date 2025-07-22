class Solution:
    def freq_char(self, s):
        output = {}
        for i in s:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1
        return output

s = "hello"
sol = Solution()
print(sol.freq_char(s))