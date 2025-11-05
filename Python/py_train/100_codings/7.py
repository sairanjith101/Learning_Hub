class Solution:
    def remove_duplicate(self, nums):
        return list(set(nums))

nums = [3, 1, 2, 3, 2, 4, 1]
sol = Solution()
print(sol.remove_duplicate(nums))

# option 2 for same order will come output

class Solution:
    def remove_duplicate(self,nums):
        seen = set()
        result = []
        for i in nums:
            if i not in seen:
                result.append(i)
                seen.add(i)
        return result

nums = [3, 1, 2, 3, 2, 4, 1]
sol = Solution()
print(sol.remove_duplicate(nums))