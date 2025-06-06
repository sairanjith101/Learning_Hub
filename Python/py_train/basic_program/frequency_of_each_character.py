s = "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

class Solution:
    def frequency_counter(self, s):
        output = {}
        for i in s:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1
        return output
sol = Solution()
print(sol.frequency_counter(s))
