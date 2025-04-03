class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def size(self) -> int:
        return self.length
    
    def pop(self) -> None:
        if self.head is None:  
            return
        temp = self.head   
        self.head = self.head.next  
        temp.next = None  
        del temp  
        self.length -= 1 


    def peek(self) -> int:
        return self.head.value
    
    def display(self) -> None:
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

    def is_empty(self) -> bool:
        return self.head is None
    

if __name__ == "__main__":
    stack = Stack()
    print("1. Push\n2. Pop\n3. Peek\n4. Length\n5. Display\n6. Is Empty\n7. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to push: "))
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            print("Top element:", stack.peek())
        elif choice == 4:
            print("Length of linked list:", stack.size())
        elif choice == 5:
            stack.display()
        elif choice == 6:
            print("Is stack empty?", stack.is_empty())
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")