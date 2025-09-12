class Solution:
    def duplicates(self, nums):
        box = []
        duplicates = []
        for i in nums:
            if i not in box:
                box.append(i)
            else:
                duplicates.append(i)
        return duplicates
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.duplicates(nums))