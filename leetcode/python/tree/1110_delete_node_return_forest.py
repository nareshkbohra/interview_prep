from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root, parent, to_delete, results):
        if root is None:
            return None
        if parent in to_delete and root.val not in to_delete:
            results.append(root)
        root.left = self.helper(root.left, root.val, to_delete, results)
        root.right = self.helper(root.right, root.val, to_delete, results)

        if root.val in to_delete:
            return None
        return root

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if len(to_delete) == 0:
            if root:
                return [root]
            else:
                return []

        results = []
        self.helper(root, to_delete[0], set(to_delete), results)
        return results
