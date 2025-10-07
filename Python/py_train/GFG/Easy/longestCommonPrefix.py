from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        box = []
        for i in strs[0]:
            if i in strs[1]:
                box.append(i)
                if i in strs[2]:
                    box.append(i)
        
        dict = {}
        for j in box:
            if j in box:
                dict[j] = 1
            else:
                dict[j] += 1
        
        return dict

strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))