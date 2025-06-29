from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memory = defaultdict(lambda : 0)
        self.duplicates = []

    def helper(self, root):
        if not root:
            return ""
        result = str(root.val) + "#" + self.helper(root.left) + "#" + self.helper(root.right)
        self.memory[result] += 1
        if self.memory[result] == 2:
            self.duplicates.append(root)
        return result

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.memory = defaultdict(lambda : 0)
        self.duplicates = []
        self.helper(root)
        return self.duplicates

