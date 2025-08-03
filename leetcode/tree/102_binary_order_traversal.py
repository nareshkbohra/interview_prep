from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)
        while len(queue):
            curr_result = []
            items = len(queue)
            for _ in range(items):
                curr_node = queue.popleft()
                if not curr_node:
                    continue
                curr_result.append(curr_node.val)
                queue.append(curr_node.left)
                queue.append(curr_node.right)
            if len(curr_result):
                result.append(curr_result)

        return result
