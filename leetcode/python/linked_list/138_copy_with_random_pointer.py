from typing import Optional, Dict


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        memory = {}
        result = Node()
        temp = result
        while head:
            if head in memory:
                newNode = memory[head]
            else:
                newNode = Node(head.val)
                memory[head] = newNode
            if head.next:
                if head.next in memory:
                    newNode.next = memory[head.next]
                else:
                    nextNode = Node(head.next.val)
                    newNode.next = nextNode
            if head.random:
                if head.random in memory:
                    newNode.random = memory[head.random]
                else:
                    randomNode = Node(head.random.val)
                    newNode.random = randomNode

            temp.next = newNode
            temp = temp.next
            head = head.next

        return result.next

        return None
