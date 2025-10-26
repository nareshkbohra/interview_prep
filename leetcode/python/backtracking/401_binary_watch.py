from typing import List, Dict
from collections import defaultdict


class Solution:
    def __init__(self):
        self.binary_map: Dict[int, List[int]] = defaultdict(list)
        for i in range(60):
            ones = self.find_ones(i)
            self.binary_map[ones].append(i)

    def find_ones(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result

    def get_hrs(self, n: int) -> List[int]:
        hrs = self.binary_map[n]
        return [hr for hr in hrs if hr < 12]

    def get_minutes(self, n: int) -> List[int]:
        minutes = self.binary_map[n]
        return [minute for minute in minutes if minute < 60]

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Similar to problem 2929 in combinations, first check min led which need to be turned
        # on for hr which depend on max or minute(5). max is 3.
        min_hr = max(0, turnedOn - 5)
        max_hr = min(turnedOn, 3)
        result = []
        for hr_leds in range(min_hr, max_hr + 1):
            minute_leds = turnedOn - hr_leds
            hrs = self.get_hrs(hr_leds)
            minutes = self.get_minutes(minute_leds)
            for hr in hrs:
                for minute in minutes:
                    if minute < 10:
                        minute = f"0{minute}"
                    result.append(f"{hr}:{minute}")

        return result


s = Solution()
res = s.readBinaryWatch(1)
print(res)
