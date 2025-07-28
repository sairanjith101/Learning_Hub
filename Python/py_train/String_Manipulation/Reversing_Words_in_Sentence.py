class Solution:
    def reverse_words(self, s):
        s_split = s.split()
        return ' '.join(s_split[::-1])

# s = "the sky is blue"
# s = " hello world "
s = "a good example"
sol = Solution()
print(sol.reverse_words(s))