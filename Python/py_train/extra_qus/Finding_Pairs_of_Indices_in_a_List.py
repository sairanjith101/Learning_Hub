from itertools import combinations

class Solution:
    def findPOI(self, nums, target):
        comb = combinations(range(len(nums)), 2)  # Generate index pairs
        output = []
        for i, j in comb:
            if nums[i] + nums[j] == target:
                output.append((i, j))  # Append the index pair
        return output

nums = [2, 7, 4, 5, 3]
target = 9
sol = Solution()
print(sol.findPOI(nums, target))
