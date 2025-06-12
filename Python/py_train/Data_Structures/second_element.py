tuples = [(1, 3), (3, 2), (2, 1)]

class Solution:
    def second_element(self, tuples):
        output = []
        for key,values in tuples.items():
            sort_values = sorted(values)
            if sort_values:
                output.append(tuples)
        return output

sol = Solution()
print(sol.second_element(tuples))