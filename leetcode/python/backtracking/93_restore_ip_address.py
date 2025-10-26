from typing import List


class Solution:
    def is_valid(self, s):
        if not s:
            return False

        if len(s) > 3:
            return False

        if len(s) == 1:
            return True

        if s[0] == "0":
            return False

        if int(s) > 255:
            return False

        return True

    def dfs(self, s, index, dots, result, curr_path):
        if index >= len(s):
            return
        if dots == 0:
            if self.is_valid(s[index:]):
                curr_path.append(int(s[index:]))
                result.append(list(curr_path))
                curr_path.pop()

            return

        for i in range(4):
            base_str = s[index : index + i]
            if not self.is_valid(base_str):
                continue
            curr_path.append(int(base_str))
            self.dfs(s, index + i, dots - 1, result, curr_path)
            curr_path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        curr_path = []
        results = []
        self.dfs(s, 0, 3, results, curr_path)
        return [".".join(str(i) for i in result) for result in results]


s = Solution()
inp = "25525511135"
res = s.restoreIpAddresses(inp)
print(res)
