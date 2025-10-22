#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        i = 0
        for index, char in enumerate(arr):
            if arr[i] + char

arr = [1, 2, 3, 7, 5]
target = 12
sol = Solution()
print(sol.subarraySum(arr, target))