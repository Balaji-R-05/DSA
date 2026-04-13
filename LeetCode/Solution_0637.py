# 637. Average of Levels in Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []

        queue = deque([root])

        while queue:
            n = len(queue)
            temp = 0
            for _ in range(n):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp / n)
        return res
    
# Time Complexity: O(N)
# Space Complexity: O(M) where M is the maximum number of nodes at any level