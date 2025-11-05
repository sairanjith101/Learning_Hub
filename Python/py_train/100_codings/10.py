from itertools import combinations

class Solution:
    def Maximum_Product(self, nums):
        product = []
        for a,b in combinations(nums, 2):
            product.append(a*b)
        return max(product)

nums = [3, 4, 5, 2]
sol = Solution()
print(sol.Maximum_Product(nums))