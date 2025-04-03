# Kosakosa Linkedlist

# Write a program to create linked list by appending the elements without its duplicate and print the resultant linked list and also the mid element of the linked list.
# Input Format
# Input consists of a single line of elements that belongs to the linked list.
# Output Format
# Output should be formatted in 2 lines : First line should be the linked list Second line should be the mid element of the linked list.

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.elements = set()
    
    def append(self, value):
        if value in self.elements:
            return
        
        self.elements.add(value)
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
    
    def mid(self):
        if not self.head:
            return None  
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value  
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

# Input and Execution
lst = list(map(int, input().split()))
ll = LinkedList()
for i in lst:
    ll.append(i)

ll.display()
print(ll.mid())