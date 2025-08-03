from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        length = len(flowerbed)
        for i in range(length):
            flowerbed = flowerbed
            if flowerbed[i] == 1:
                continue

            previous_free = i == 0 or flowerbed[i - 1] == 0
            if not previous_free:
                continue

            next_free = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if not next_free:
                continue

            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True

        return False
