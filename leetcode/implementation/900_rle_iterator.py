from typing import List
from bisect import bisect_left


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.number = [encoding[1]]
        self.freq = [encoding[0]]

        for i in range(2, len(encoding), 2):
            (freq, num) = encoding[i], encoding[i + 1]
            self.number.append(num)
            self.freq.append(freq + self.freq[-1])

        self.consumed = 0

    def next(self, n: int) -> int:
        if self.consumed >= self.freq[-1]:
            return -1

        self.consumed = n + self.consumed
        if self.consumed > self.freq[-1]:
            return -1

        index = bisect_left(self.freq, self.consumed)
        return self.number[index]
