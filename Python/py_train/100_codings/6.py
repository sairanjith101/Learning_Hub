class Solution:
    def second_largest(self, nums):
        n = sorted(set(nums))
        if len(n) > 1:
            return n[-2]
        return n[-1]
    
nums = [8, 1, 9, 9, 3, 8, 7]
sol = Solution() 
print(sol.second_largest(nums))