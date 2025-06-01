from typing import Optional


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def helper(self, root: Optional[TreeNode], limit: int, curr_sum: int) -> Optional[TreeNode]:
		if root is None:
			return None
		curr_sum += root.val
		if root.left is None and root.right is None:
			if curr_sum < limit:
				return None
			return root

		root.left = self.helper(root.left, limit, curr_sum)
		root.right = self.helper(root.right, limit, curr_sum)
		if root.left is None and root.right is None:
			return None
		return root

	def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
		return self.helper(root, limit, 0)
