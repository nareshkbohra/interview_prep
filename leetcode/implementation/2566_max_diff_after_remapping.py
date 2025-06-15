class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        # First calculate max number. that should be by replacing first non-9 number
        max_str = str(num)
        for ch in num_str:
            if ch != "9":
                max_str = num_str.replace(ch, "9")
                break

        max_num = int(max_str)
        min_num = int(num_str.replace(num_str[0], "0"))
        return max_num - min_num


num = 90
s = Solution()
res = s.minMaxDifference(num)
print(res)
