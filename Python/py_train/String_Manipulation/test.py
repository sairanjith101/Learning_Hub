class Solution:
    def reverse_word(self, s):
        split_s = s.split()
        return ' '.join(split_s[::-1])

s = "the sky is blue"
sol = Solution()
print(sol.reverse_word(s))