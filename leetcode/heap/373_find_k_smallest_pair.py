from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = [(nums1[0] + nums2[1], 0, 0)]
        visited = set()
        while heap and len(result) < k:
            _, x, y = heapq.heappop(heap)
            result.append([nums1[x], nums2[y]])

            if x + 1 < len(nums1) and (x + 1, y) not in visited:
                heapq.heappush(heap, (nums1[x + 1] + nums2[y], x + 1, y))
                visited.add((x + 1, y))

            if y + 1 < len(nums2) and (x, y + 1) not in visited:
                heapq.heappush(heap, (nums1[x] + nums2[y + 1], x, y + 1))
                visited.add((x, y + 1))

        return result
