from typing import Optional
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


MIN_VALUE = -sys.maxsize


class Solution:
    def helper(self, root: Optional[TreeNode], max_value: int) -> int:
        if root is None:
            return 0
        result = 0
        if root.val >= max_value:
            result = 1
        max_value = max(root.val, max_value)
        result += self.helper(root.left, max_value)
        result += self.helper(root.right, max_value)
        return result

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, MIN_VALUE)
