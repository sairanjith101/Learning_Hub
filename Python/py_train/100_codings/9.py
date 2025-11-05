class Solution:
    def Rotate_List_using_key(self, nums, k):
        result = []
        while True:
            nums = nums[-1:] + nums[:-1]
            k=k-1
            if k == 0:
                result = nums
                break
        return result


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution() 
print(sol.Rotate_List_using_key(nums, k))