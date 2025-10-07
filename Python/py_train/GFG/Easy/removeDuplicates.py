from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for unique elements
        k = 1
        for i in range(1, len(nums)):
            # If the current number is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # place it in the 'unique' section
                k += 1
        
        return k

# Example 1
nums = [1, 1, 2]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k, nums[:k])   # Output: 2 [1, 2]

# Example 2
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)
print(k, nums[:k])   # Output: 5 [0, 1, 2, 3, 4]


# details

# nums[k] = nums[i]
# nums[1] = nums[2]
# nums[1] = 2
# nums = [1, 2, 2]
