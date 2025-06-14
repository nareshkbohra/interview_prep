from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0]
        for interval in intervals[1:]:
            curr_start, curr_end = interval
            if curr_start <= end:
                end = max((end, curr_end))
            else:
                result.append([start, end])
                start = curr_start
                end = curr_end

        result.append([start, end])
        return result


s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
res = s.merge(intervals)
print(res)
