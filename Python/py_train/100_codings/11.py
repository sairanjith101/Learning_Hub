class Solution:
    def Count_Frequency_of_Elements(self, nums):
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        return dict

# nums = [1, 2, 2, 3, 1, 4]
nums = []
sol = Solution()
print(sol.Count_Frequency_of_Elements(nums))