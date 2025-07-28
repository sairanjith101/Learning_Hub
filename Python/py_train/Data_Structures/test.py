class Solution:
    def sortlistoftuple(self, tuples):
        my_dict = dict(tuples)
        output = []
        for key,values in my_dict.items():
            sort_value = values.sort()
            if sort_value:
                output.append(tuples)
        return output

tuples = [(1, 3), (3, 2), (2, 1)]
sol = Solution()
print(sol.sortlistoftuple(tuples))