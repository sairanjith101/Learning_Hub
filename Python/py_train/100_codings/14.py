class Solution:
    def Convert_List_of_Tuples_Into_Dict(self, pairs):
        # case 1
        dict = {}
        for key, value in pairs:
            dict[key] = value
        return dict
    
        # case 2
        # return dict(pairs)

pairs = [("a", 1), ("b", 2), ("c", 3)]
sol = Solution()
print(sol.Convert_List_of_Tuples_Into_Dict(pairs))