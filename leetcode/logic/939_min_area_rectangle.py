from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_collection = set()
        for point in points:
            point_collection.add(tuple(point))

        min_area = float("inf")

        for i in range(len(points)):
            f_x, f_y = points[i]
            for j in range(i + 1, len(points)):
                s_x, s_y = points[j]
                if f_x == s_x or f_y == s_y:
                    continue

                first = (f_x, s_y)
                if first not in point_collection:
                    continue

                second = (s_x, f_y)
                if second not in point_collection:
                    continue

                area = abs((f_y - s_y) * (f_x - s_x))
                min_area = min((area, min_area))

        if min_area == float("inf"):
            return 0
        return int(min_area)


s = Solution()
points = [[3, 2], [3, 1], [4, 4], [1, 1], [4, 3], [0, 3], [0, 2], [4, 0]]
res = s.minAreaRect(points)
print(res)
