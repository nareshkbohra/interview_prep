from typing import Optional, List
from collections import deque
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val} {self.left} {self.right}"


MIN_VAL = -sys.maxsize


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        sentinel = TreeNode()
        max_value = MIN_VAL
        queue = deque([root, sentinel])
        while len(queue) > 1:
            curr_node = queue.popleft()
            if curr_node is None:
                continue

            if curr_node is sentinel:
                result.append(max_value)
                queue.append(sentinel)
                max_value = MIN_VAL
                continue

            max_value = max(max_value, curr_node.val)
            queue.append(curr_node.left)
            queue.append(curr_node.right)
        return result


node_a = TreeNode(5)
node_b = TreeNode(3)
node_c = TreeNode(9)
node_d = TreeNode(3, node_a, node_b)
node_e = TreeNode(2, None, node_c)
node_f = TreeNode(1, node_d, node_e)

s = Solution()
res = s.largestValues(node_f)
print(" ".join(str(i) for i in res))
