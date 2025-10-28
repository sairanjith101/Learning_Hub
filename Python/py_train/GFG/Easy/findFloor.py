class Solution:
    def findFloor(self, arr, x):
        # code here
        box = []
        for index, char in enumerate(arr):
            if char <= x:
                box.append(index)
        if box:
            return max(box)
        return -1

arr = [1, 2, 8, 10, 10, 12, 19]
x = 11
sol = Solution()
print(sol.findFloor(arr, x))