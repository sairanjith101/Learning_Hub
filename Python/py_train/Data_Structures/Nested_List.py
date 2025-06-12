nested_list = [1, [2, [3, 4], 5], 6]

class Solution:
    def NestedList(self, nested_list):
        output = []
        for i in nested_list:
            if isinstance(i, int):
                output.append(i)
            elif isinstance(i, list):
                output.extend(self.NestedList(i))  # recursively flatten inner list
        return output

sol = Solution()
print(sol.NestedList(nested_list))
