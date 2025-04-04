class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build(self, input_data):
        if not input_data or input_data[0] == -1:
            return

        self.root = TreeNode(input_data[0])
        queue = [self.root]
        i = 1

        while queue and i < len(input_data):
            current = queue.pop(0)

            if i < len(input_data) and input_data[i] != -1:
                current.left = TreeNode(input_data[i])
                queue.append(current.left)
            i += 1

            if i < len(input_data) and input_data[i] != -1:
                current.right = TreeNode(input_data[i])
                queue.append(current.right)
            i += 1


    def inorder(self):
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            print(node.value, end=' ')
            inorder(node.right)

        inorder(self.root)
        
        
    def preorder(self):
        def preorder(node):
            if not node:
                return
            print(node.value, end=' ')
            preorder(node.left)
            preorder(node.right)

        preorder(self.root)


    def postorder(self):
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            print(node.value, end=' ')

        postorder(self.root)
        

    def bfs(self):
        queue = [self.root]
        while queue:
            data = queue.pop(0)
            print(data.value, end=" ")
            if data.left is not None and data.left!=-1:
                queue.append(data.left)
            if data.right is not None and data.right!=-1:
                queue.append(data.right)
                
    def size(self):
        def count(root):
            if root is None:
                return 0
            return 1 + count(root.left) + count(root.right)
    
        return count(self.root)



       
                
def main():
    input_data = list(map(int, input().split()))
    tree = BinaryTree()
    tree.build(input_data)
    tree.inorder()
    tree.preorder()
    tree.postorder()
    tree.bfs()

if __name__ == "__main__":
    main()
