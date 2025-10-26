from typing import List


class Solution:
    def leading_ones(self, num):
        result = 0
        for i in range(7, -1, -1):
            if not (num & 1 << i):
                return result
            result += 1

        return result

    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            no_of_ones = self.leading_ones(data[i])
            if no_of_ones == 0:
                i += 1
                continue

            if no_of_ones == 1:
                return False

            if no_of_ones > 4:
                return False

            i += 1

            for _ in range(no_of_ones - 1):
                if i >= len(data):
                    return False
                next_ones = self.leading_ones(data[i])
                if next_ones != 1:
                    return False
                i += 1

        return True


s = Solution()
data = [250, 145, 145, 145, 145]
res = s.validUtf8(data)
print(res)
