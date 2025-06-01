from typing import Optional, List
from itertools import chain


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def helper(self, root: Optional[TreeNode]) -> List[str]:
		if root is None:
			return []

		left = self.helper(root.left)
		right = self.helper(root.right)
		root_val = chr(root.val + ord("a"))
		result = [res + root_val for res in chain(left, right)]

		if not result:
			result = [root_val]

		return result

	def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
		return min(self.helper(root))
