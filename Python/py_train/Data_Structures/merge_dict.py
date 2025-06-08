dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Output: {"a": 1, "b": 3, "c": 4}

class Solution:
    def mergedict(self, dict1, dict2):
        dict1.update(dict2)
        return dict1

sol = Solution()
print(sol.mergedict(dict1, dict2))