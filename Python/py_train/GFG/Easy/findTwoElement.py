class Solution:
    def findTwoElement(self, arr):
        box = {}
        repeat_num = 0
        missing_num = 0
        
        # Find repeating number
        for num in arr:
            if num in box:
                repeat_num = num
            else:
                box[num] = 1
        
        # Find missing number
        n = len(arr)
        for i in range(1, n+1):
            if i not in box:
                missing_num = i
                break
        
        return [repeat_num, missing_num]


arr = [5,1,6,2,4,6]
sol = Solution()
print(sol.findTwoElement(arr))  # Output: [6, 3]
