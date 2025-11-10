from collections import defaultdict

class Solution:
    def Anagrams(self, words):
        box = defaultdict(list)
        for word in words:
            box[''.join(sorted(word))].append(word)
        return list(box.values())

words = ["bat", "tab", "tap", "pat", "cat"]
sol = Solution()
print(sol.Anagrams(words))