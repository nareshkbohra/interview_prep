from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentToFile = defaultdict(list)
        for currPath in paths:
            currPath = currPath.split(" ")
            root = currPath[0]
            for file in currPath[1:]:
                file = file.split("(")
                fileName = file[0]
                content = file[1][:-1]
                contentToFile[content].append(f"{root}/{fileName}")
        result = []
        for _, paths in contentToFile.items():
            if len(paths) > 1:
                result.append(paths)

        return result
