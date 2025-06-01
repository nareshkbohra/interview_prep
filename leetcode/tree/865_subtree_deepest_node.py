from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self) -> str:
		return f"{self.val} {self.left} {self.right}"


class Solution:
	def helper(self, root: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
		if root is None:
			return None, 0
		leftNode, leftDepth = self.helper(root.left)
		rightNode, rightDepth = self.helper(root.right)
		if leftDepth == rightDepth:
			return (root, leftDepth + 1)

		if leftDepth < rightDepth:
			return (rightNode, rightDepth + 1)

		return (leftNode, leftDepth + 1)

	def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		res, _ = self.helper(root)
		return res


node7 = TreeNode(7)
node4 = TreeNode(4)
node0 = TreeNode(0)
node8 = TreeNode(8)
node1 = TreeNode(1, node0, node8)
node2 = TreeNode(2, node7, node4)
node6 = TreeNode(6)
node5 = TreeNode(5, node6, node2)
node3 = TreeNode(3, node5, node1)


s = Solution()
res = s.subtreeWithAllDeepest(node3)
print(res)
