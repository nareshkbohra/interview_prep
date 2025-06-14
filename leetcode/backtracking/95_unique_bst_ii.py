from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, start, end) -> List[Optional[TreeNode]]:
        key = (start, end)
        if key in self.memory:
            return self.memory[key]
        if start > end:
            return [None]

        result: List[Optional[TreeNode]] = []
        for i in range(start, end + 1):
            left = self.helper(start, i - 1)
            right = self.helper(i + 1, end)
            for left_tree in left:
                for right_tree in right:
                    new_node = TreeNode(i, left_tree, right_tree)
                    result.append(new_node)

        self.memory[key] = result
        return result

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.memory = {}
        return self.helper(0, n)
