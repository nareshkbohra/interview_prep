from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        sectionSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rowSet[i]:
                    return False
                rowSet[i].add(num)

                if num in colSet[j]:
                    return False
                colSet[j].add(num)

                section = (i // 3, j // 3)
                if num in sectionSet[section]:
                    return False
                sectionSet[section].add(num)

        return True
