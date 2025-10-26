from typing import List, Dict
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - First prepare below things
            1. For each course how many dependencies are there.
            2. For each course list of dependents.
        - Now iterate over number of dependency array and put all the elements with zero
          dependency in queue
        - For each element in queue, reduce one count in dependents. If dependents reach 0 then
          push them into queue.
        - After each course count, increase complete course count.
        - Check complete course count is same as numCourses
        """
        dependencyCount = [0] * numCourses
        graph: Dict[int, List[int]] = defaultdict(list)

        for start, end in prerequisites:
            dependencyCount[start] += 1
            graph[end].append(start)

        queue = deque()
        for idx, dependency in enumerate(dependencyCount):
            if dependency == 0:
                queue.append(idx)

        completedCourse = 0
        while len(queue):
            curr_course = queue.popleft()
            completedCourse += 1
            for dependent in graph[curr_course]:
                dependencyCount[dependent] -= 1
                if dependencyCount[dependent] == 0:
                    queue.append(dependent)

        return completedCourse == numCourses


s = Solution()
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
res = s.canFinish(numCourses, prerequisites)
print(res)
