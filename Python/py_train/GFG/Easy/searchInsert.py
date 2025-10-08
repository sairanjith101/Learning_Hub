from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)  # insert at the end if not found

# nums = [1,3,5,6]
# target = 0
nums = [1001]
target = 5
sol = Solution()
print(sol.searchInsert(nums, target))