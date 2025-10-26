from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        history = self.values[key]
        left = 0
        right = len(history)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if history[mid] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans < 0:
            return ""
        return history[ans][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
