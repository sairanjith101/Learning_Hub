from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

nums = [3,2,2,3]
val = 3
sol = Solution()
k = sol.removeElement(nums, val)
print(k, nums[:k])