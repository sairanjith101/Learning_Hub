nums = [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

class Solution:
    def removeduplicates(self, nums):
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
        return unique
    
sol = Solution()
print(sol.removeduplicates(nums))