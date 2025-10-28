#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        set1,set2,set3 = set(arr1),set(arr2),set(arr3)
        box = []
        for i in set1:
            if i in set2 and i in set3:
                box.append(i)
        if box:
            return sorted(box)
        return -1

arr1 = [1, 1, 1, 2, 2, 2]
arr2 = [1, 1, 2, 2, 2]
arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
sol = Solution()
print(sol.commonElements(arr1,arr2,arr3))