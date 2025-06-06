nums = [3, 1, 7, 2, 9, 5]

class Solution:
    def larsmal(self, nums):
        return [min(nums), max(nums)]

sol = Solution()
print(sol.larsmal(nums))