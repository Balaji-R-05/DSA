# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            if root:
                res.append(root.val)
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        return res
    
# Time complexity: O(n)
# Space complexity: O(n)