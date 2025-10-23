class Solution:
    def binarysearch(self, arr, k):
        for index,char in enumerate(arr):
            if char == k:
                return index
        return -1

arr = [1, 1, 1, 1, 2]
k = 1
sol = Solution()
print(sol.binarysearch(arr, k))