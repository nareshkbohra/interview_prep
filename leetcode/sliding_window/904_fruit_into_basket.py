from typing import List, Dict
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts: Dict[int, int] = defaultdict(lambda: 0)
        j = 0
        result = 0
        for i in range(len(fruits)):
            f_type = fruits[i]
            counts[f_type] += 1
            while len(counts) > 2:
                prev_type = fruits[j]
                counts[prev_type] -= 1
                if counts[prev_type] == 0:
                    counts.pop(prev_type)
                j += 1
            result = max(result, i - j + 1)

        return result


s = Solution()
inp = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
res = s.totalFruit(inp)
print(res)
