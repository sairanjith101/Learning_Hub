from itertools import combinations

class Solution:
    def Find_the_Pair(self, nums, target):
        result = []
        comb = combinations(nums, 2)
        for c in comb:
            if sum(c) == target:
                result.append(c)
        return result

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.Find_the_Pair(nums, target))