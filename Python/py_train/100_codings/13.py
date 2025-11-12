class Solution:
    def Merge_Two_Dict(self, dict1, dict2):
        dict1.update(dict2)
        return dict1

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4}
sol = Solution() 
print(sol.Merge_Two_Dict(dict1, dict2))