class Solution:
    def findduplicate(self, nums):
        output = []
        duplicate = []
        for i in nums:
            if i not in output:
                output.append(i)
            else:
                duplicate.append(i)
        return duplicate 
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findduplicate(nums))