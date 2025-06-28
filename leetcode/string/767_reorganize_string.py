import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)
        result = ""
        while heap:
            (count, char) = heapq.heappop(heap)

            if not heap:
                if count != -1:
                    return ""
                else:
                    result += char
                    return result
            (secondCount, secondChar) = heapq.heappop(heap)
            result += char
            result += secondChar
            if count + 1 < 0:
                heapq.heappush(heap, (count + 1, char))
            if secondCount + 1 < 0:
                heapq.heappush(heap, (secondCount + 1, secondChar))

        return result


s = Solution()
res = s.reorganizeString("abbc")
print(res)
