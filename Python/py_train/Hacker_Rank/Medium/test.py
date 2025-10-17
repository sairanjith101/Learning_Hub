from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = l1[::-1]
        l2 = l2[::-1]
        reversed_l1 = int(''.join(map(str, l1)))
        reversed_l2 = int(''.join(map(str, l2)))
        l = reversed_l1 + reversed_l2
        new_list = list(map(int, str(l)))
        return new_list[::-1]

# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [0]
# l2 = [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
sol = Solution()
print(sol.addTwoNumbers(l1,l2))