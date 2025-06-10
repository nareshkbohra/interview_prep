from typing import List, Dict
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        result = []
        while len(queue):
            curr_course = queue.popleft()
            completedCourse += 1
            result.append(curr_course)
            for dependent in graph[curr_course]:
                dependencyCount[dependent] -= 1
                if dependencyCount[dependent] == 0:
                    queue.append(dependent)

        if completedCourse != numCourses:
            return []
        return result


s = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
res = s.findOrder(numCourses, prerequisites)
print(res)
