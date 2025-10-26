# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root):
        if root is None:
            return True, float("inf"), -float("inf")

        leftBST, leftMin, leftMax = self.helper(root.left)
        if not leftBST or leftMax >= root.val:
            return False, -1, -1

        rightBST, rightMin, rightMax = self.helper(root.right)
        if not rightBST or rightMin <= root.val:
            return False, -1, -1

        return True, min(leftMin, root.val), max(rightMax, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]
