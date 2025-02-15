# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
    
        # Attach remaining nodes
        current.next = list1 if list1 else list2    
        return dummy.next
    
# Time complexity: O(n + m)
# Space complexity: O(1)

# The algorithm merges two sorted linked lists.
# The algorithm initializes a dummy node and a current node.
# The algorithm iterates over the two linked lists.
# The algorithm compares the values of the two nodes.
# The algorithm attaches the smaller node to the current node.
# The algorithm updates the current node.
# The algorithm attaches the remaining nodes to the current node.
# The algorithm returns the merged linked list.

solution = Solution()
print(solution.mergeTwoLists([1,2,4], [1,3,4])) # [1,1,2,3,4,4]
print(solution.mergeTwoLists([], [])) # []
print(solution.mergeTwoLists([], [0])) # [0]
print(solution.mergeTwoLists([1,2,4], [])) # [1,2,4]