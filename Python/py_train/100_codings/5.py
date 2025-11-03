class Solution:
    def First_Non_Repeating_Char(self, str):
        box = {}
        for i in str:
            if i not in box:
                box[i] = 1
            else:
                box[i] += 1
        
        for key,value in box.items():
            if value == 1:
                return key
        return -1

str = "aabb"
sol = Solution()
print(sol.First_Non_Repeating_Char(str))