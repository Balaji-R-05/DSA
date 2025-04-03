class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.length = 0
        self.last = None

    def enqueue(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1

    def size(self) -> int:
        return self.length
    
    def dequeue(self) -> None:
        self.head = self.head.next
        self.length -= 1

    def peek(self) -> int:
        return self.last.value
    
    def display(self) -> None:
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

    def is_empty(self) -> bool:
        return self.head is None
    

if __name__ == "__main__":
    queue = Queue()
    print("1. Enqueue\n2. Dequeue\n3. Peek\n4. Length\n5. Display\n6. Is Empty\n7. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to enqueue: "))
            queue.enqueue(data)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            print("Top element:", queue.peek())
        elif choice == 4:
            print("Length of linked list:", queue.size())
        elif choice == 5:
            queue.display()
        elif choice == 6:
            print("Is Queue empty?", queue.is_empty())
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")