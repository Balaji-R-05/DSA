class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: get inorder successor (smallest in right subtree)
            min_node = self.getMin(root.right)
            root.val = min_node.val  # Copy successor's value to current node
            root.right = self.deleteNode(root.right, min_node.val)  # Delete successor

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
    
    def getMax(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node
