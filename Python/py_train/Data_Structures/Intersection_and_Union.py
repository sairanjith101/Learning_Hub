list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 5]

# Output: Intersection: [2, 3], Union: [1, 2, 3, 4, 5]

class Solution:
    def intersectionandunion(self, list1, list2):
        list1 = set(list1)
        list2 = set(list2)
        union = list(list1 | list2)
        intersection = []
        for i in list1:
            if i in list2:
                intersection.append(i)
        return union, intersection
        

sol = Solution()
print(sol.intersectionandunion(list1, list2))