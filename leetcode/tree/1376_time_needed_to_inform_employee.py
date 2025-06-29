from typing import List


class Node:
    def __init__(self, informTime):
        self.children = []
        self.informTime = informTime


class Solution:
    def waitTime(self, root: Node):
        if root is None or len(root.children) == 0:
            return 0
        childrenInform = max(self.waitTime(child) for child in root.children)

        return root.informTime + childrenInform

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        memory = {}
        for empId, managerId in enumerate(manager):
            if empId not in memory:
                memory[empId] = Node(informTime[empId])
            emp = memory[empId]

            if managerId not in memory:
                memory[managerId] = Node(informTime[managerId])
            managerObj = memory[managerId]

            managerObj.children.append(emp)

        return self.waitTime(memory[headID])
