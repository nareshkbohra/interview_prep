class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = [int(i) for i in version1.split(".")]
        second = [int(i) for i in version2.split(".")]
        first_len, second_len = len(first), len(second)
        if first_len < second_len:
            first.extend([0] * (second_len - first_len))
        elif second_len < first_len:
            second.extend([0] * (first_len - second_len))
        if first < second:
            return -1
        if second < first:
            return 1
        return 0


version1 = "1.0"
version2 = "1.0.0.0"
s = Solution()
res = s.compareVersion(version1, version2)
print(res)
