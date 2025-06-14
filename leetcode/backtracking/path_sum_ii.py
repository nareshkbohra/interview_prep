from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root, targetSum, currPath, results):
        if root is None:
            return
        currPath.append(root.Val)
        if root.Left == root.Right:
            if root.Val == targetSum:
                results.append(list(currPath))
            currPath.pop()
            return

        newTarget = targetSum - root.Val
        self.helper(root.Left, newTarget, currPath, results)
        self.helper(root.Right, newTarget, currPath, results)

        currPath.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        currPath = []
        results = []
        self.helper(root, targetSum, currPath, results)
        return results
