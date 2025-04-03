class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def isPalindrome(self):
        if not self.head or not self.head.next:
            return True
        
        
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        
        left, right = self.head, prev
        while right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next
        
        return True


elements = list(map(int, input().split()))
ll = LinkedList()

for val in elements:
    if val == -1:
        break
    ll.append(val)

print("true" if ll.isPalindrome() else "false")
