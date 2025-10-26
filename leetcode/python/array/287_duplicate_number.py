from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)
        return -1
