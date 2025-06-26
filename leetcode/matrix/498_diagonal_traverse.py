from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        elements = rows * cols
        covered = 0
        currentNode = (0, 0)

        def isValid(point):
            a, b = point
            return 0 <= a < rows and 0 <= b < cols

        result = []
        while covered < elements:
            # Going up path
            while True:
                covered += 1
                result.append(mat[currentNode[0]][currentNode[1]])

                nextNode = currentNode[0] - 1, currentNode[1] + 1
                if isValid(nextNode):
                    currentNode = nextNode
                    continue

                nextNode = currentNode[0], currentNode[1] + 1
                if isValid(nextNode):
                    currentNode = nextNode
                    break

                nextNode = currentNode[0] + 1, currentNode[1]
                if isValid(nextNode):
                    currentNode = nextNode
                    break

                return result

            # Going down path
            while True:
                covered += 1
                result.append(mat[currentNode[0]][currentNode[1]])

                nextNode = currentNode[0] + 1, currentNode[1] - 1
                if isValid(nextNode):
                    currentNode = nextNode
                    continue

                nextNode = currentNode[0] + 1, currentNode[1]
                if isValid(nextNode):
                    currentNode = nextNode
                    break

                nextNode = currentNode[0], currentNode[1] + 1
                if isValid(nextNode):
                    currentNode = nextNode
                    break

                return result

        return []


mat = [[1, 2], [3, 4]]
s = Solution()
res = s.findDiagonalOrder(mat)
print(res)
s = Solution()
