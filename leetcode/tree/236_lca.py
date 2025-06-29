# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find(self, root, p):
        if not root:
            return None
        if p.val == root.val:
            return [root]
        inLeft = self.find(root.left, p)
        result = [root]
        if inLeft:
            result.extend(inLeft)
            return result

        inRight = self.find(root.right, p)
        if inRight:
            result.extend(inRight)
            return result

        return None

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        leftPath = self.find(root, p)
        rightPath = self.find(root, q)
        result = root
        for left, right in zip(leftPath, rightPath):
            if left.val != right.val:
                break
            result = left
        return result
