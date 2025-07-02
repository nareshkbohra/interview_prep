from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        previousNode = None
        queue = deque([root])
        while len(queue):
            queueSize = len(queue)
            for _ in range(queueSize):
                currNode = queue.popleft()
                if not currNode:
                    continue
                if previousNode:
                    previousNode.right = currNode
                previousNode = currNode
                queue.append(currNode.left)
                queue.append(currNode.right)
            previousNode = None

        return root
