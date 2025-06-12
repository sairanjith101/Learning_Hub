nums = [3, 2, 1, 5, 6, 4]

class Solution:
    def secondlargest(self, nums):
        num_sort = sorted(list(set(nums)))
        if len(num_sort) < 2:
            return -1
        return num_sort[-2]

sol = Solution()
print(sol.secondlargest(nums))