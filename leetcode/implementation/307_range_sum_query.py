from typing import List


class Node:
    def __init__(self, start, end, total=0):
        self.start = start
        self.end = end

        self.left = None
        self.right = None

        self.total = total


class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.createTree(nums, 0, len(nums) - 1)

    def createTree(self, nums, left, right):
        if left > right:
            return None

        if left == right:
            return Node(left, right, nums[left])

        mid = (left + right) // 2
        root = Node(left, right)
        root.left = self.createTree(nums, left, mid)
        root.right = self.createTree(nums, mid + 1, right)
        root.total = root.left.total + root.right.total
        return root

    def updateHelper(self, root, index, val):
        if root.start == root.end:
            root.total = val
            return

        mid = (root.start + root.end) // 2
        if index <= mid:
            self.updateHelper(root.left, index, val)
        else:
            self.updateHelper(root.right, index, val)

        root.total = root.left.total + root.right.total

    def update(self, index: int, val: int) -> None:
        self.updateHelper(self.root, index, val)

    def sumRangeHelper(self, root, left, right):
        if root.start == left and root.end == right:
            return root.total

        mid = (root.start + root.end) // 2
        if right <= mid:
            return self.sumRangeHelper(root.left, left, right)

        if left >= mid + 1:
            return self.sumRangeHelper(root.right, left, right)

        return self.sumRangeHelper(root.left, left, mid) + self.sumRangeHelper(root.right, mid + 1, right)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeHelper(self.root, left, right)
