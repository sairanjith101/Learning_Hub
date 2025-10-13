from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        digits1 = []
        for i in nums1:
            if i != 0:
                digits1.append(i)
        digits2 = []
        for j in nums2:
            if j !=0:
                digits2.append(j)
        new = sorted(digits1+digits2)
        return new
        

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol = Solution()
print(sol.merge(nums1, m, nums2, n))