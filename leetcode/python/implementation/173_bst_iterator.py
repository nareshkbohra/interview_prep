from typing import Optional


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.next = next(self.iter, None)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        res, self.next = self.next, next(self.iter, None)
        return res

    def hasNext(self) -> bool:
        return self.next is not None
