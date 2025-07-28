class Solution:
    def reverse_word(self, s):
        split_s = s.strip().split()
        return ' '.join(split_s[::-1])

# s = "the sky is blue"
s = " hello world "
sol = Solution()
print(sol.reverse_word(s))