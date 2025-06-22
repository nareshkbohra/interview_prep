from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        result = Node(node.val)
        memory = {node.val: result}
        visited = set()

        queue = deque([node])
        while len(queue):
            currNode = queue.popleft()
            if currNode.val in visited:
                continue
            visited.add(currNode.val)

            if currNode.val not in memory:
                copyNode = Node(currNode.val)
            else:
                copyNode = memory[currNode.val]

            for neighbor in currNode.neighbors:
                if neighbor.val in memory:
                    newNode = memory[neighbor.val]
                else:
                    newNode = Node(neighbor.val)
                    memory[neighbor.val] = newNode
                copyNode.neighbors.append(newNode)
                queue.append(neighbor)

        return result


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node3)

node2.neighbors.append(node1)
node2.neighbors.append(node4)

node3.neighbors.append(node1)
node3.neighbors.append(node4)

node4.neighbors.append(node2)
node4.neighbors.append(node3)

s = Solution()
res = s.cloneGraph(node1)
print(res)
