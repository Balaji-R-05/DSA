# 653. Two Sum IV - Input is a BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        res = []
        def helper(node):
            if node:
                res.append(node.val)
                helper(node.left)
                helper(node.right)

        helper(root)

        if len(res) == 1:
            return False
        for i in range(len(res)):
            for j in range(i+1, len(res)):
                if res[i] + res[j] == k:
                    return True
        return False
    
        map = {}

        for i in range(len(res)):
            num = k - res[i]
            if num in map:
                return True
            map[res[i]] = i
        return False

# Time Complexity: O(n^2)
# Space Complexity: O(n)