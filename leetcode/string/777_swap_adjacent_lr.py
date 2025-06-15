class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        """
        1. Pattern of L and R should be same
        2. L in start should be less than result
        3. R in start should be more than result
        """
        if start.replace("X", "") != result.replace("X", ""):
            return False
        start_index = [(index, ch) for index, ch in enumerate(start) if ch != "X"]
        result_index = [(index, ch) for index, ch in enumerate(result) if ch != "X"]
        for (s_index, s_ch), (r_index, r_ch) in zip(start_index, result_index):
            if s_ch == "L" and s_index < r_index:
                return False
            elif s_ch == "R" and s_index > r_index:
                return False
        return True


s = Solution()
start = "RXXLRXRXL"
result = "XRLXXRRLX"
res = s.canTransform(start, result)
print(res)
