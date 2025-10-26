from typing import List
import sys


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        If either top or bottom need to same, this will be based on first top/bottom
        So first check if top and bottom are present in all the pairs.
        If not return -1.
        So whichever is present calculate:
                count of that in top line
                calculate len(tops) - count
                result is min of both
        """
        top, bottom = tops[0], bottoms[0]
        top_missing = False
        bottom_missing = False
        all_missing = False
        for pair in zip(tops, bottoms):
            if top not in pair:
                top_missing = True
            if bottom not in pair:
                bottom_missing = True
            if all((top_missing, bottom_missing)):
                all_missing = True
                break

        print(top_missing, bottom_missing)
        if all_missing:
            return -1
        top_result = sys.maxsize
        if not top_missing:
            top_count_1 = len(tops) - tops.count(top)
            top_count_2 = len(tops) - bottoms.count(top)
            top_result = min(top_count_1, top_count_2)
        bottom_result = sys.maxsize
        if not bottom_missing:
            bottom_count_1 = len(tops) - tops.count(bottom)
            bottom_count_2 = len(tops) - bottoms.count(bottom)
            bottom_result = min(bottom_count_1, bottom_count_2)
        return min(top_result, bottom_result)


s = Solution()
tops = []
bottoms = []
res = s.minDominoRotations(tops, bottoms)
print(res)
