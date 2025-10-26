from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, root):
        if not root:
            return 0
        if root in self.memory:
            return self.memory[root]

        withRootValue = root.val
        if root.left:
            withRootValue += self.helper(root.left.left) + self.helper(root.left.right)
        if root.right:
            withRootValue += self.helper(root.right.left) + self.helper(root.right.right)

        leftValue = self.helper(root.left)
        rightValue = self.helper(root.right)
        result = max(leftValue + rightValue, withRootValue)
        self.memory[root] = result
        return result

    def rob(self, root: Optional[TreeNode]) -> int:
        self.memory = {}
        return self.helper(root)
