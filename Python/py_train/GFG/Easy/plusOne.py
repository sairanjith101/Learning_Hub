from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        return [int(i) for i in str(num)]

# digits = [1,2,3]
digits = [100]
sol = Solution()
print(sol.plusOne(digits))

