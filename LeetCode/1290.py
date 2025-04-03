# 1290. Convert Binary Number in a Linked List to Integer

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        
        return int(s,2)
    
# Time complexity: O(n)
# Space complexity: O(1)