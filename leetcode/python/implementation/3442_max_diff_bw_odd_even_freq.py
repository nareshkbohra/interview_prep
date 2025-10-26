from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_odd_freq = 0
        min_even_freq = float("inf")
        for ch, count in counts.items():
            if count % 2 == 1:
                max_odd_freq = max(max_odd_freq, count)
            else:
                min_even_freq = min(min_even_freq, count)
        return max_odd_freq - int(min_even_freq)


s = Solution()
res = s.maxDifference("aaaaabbc")
print(res)
