from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = [(-count, word) for word, count in Counter(words).items()]
        heapq.heapify(word_counter)
        result = [heapq.heappop(word_counter)[1] for _ in range(k)]
        return result
