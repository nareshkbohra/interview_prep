class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]

            start = max(first[0], second[0])
            end = min(first[1], second[1])
            if start <= end:
                result.append([start, end])

            if first[1] > second[1]:
                j += 1
            elif second[1] > first[1]:
                i += 1
            else:
                i += 1
                j += 1

        return result
