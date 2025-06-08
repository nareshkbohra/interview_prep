import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for index, ch in enumerate(s):
            if ch == "*":
                a = heapq.heappop(heap)
            else:
                heapq.heappush(heap, (ch, -index))
        heap = sorted(heap, key=lambda x: x[1])
        return "".join(str(i[0]) for i in reversed(heap))


s = Solution()
res = s.clearStars("daaba*")
print(res)
