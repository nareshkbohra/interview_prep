class Solution:
    def lengthLongestPath(self, input: str) -> int:
        result = 0
        folder_len = {}
        for line in input.split("\n"):
            is_file = "." in line
            tab_count = line.count("\t")
            line = line.replace("\t", "")
            line_len = len(line)
            if is_file:
                if tab_count == 0:
                    result = max(line_len, result)
                else:
                    curr_len = folder_len[tab_count - 1]
                    result = max(line_len + curr_len + 1, result)
            else:
                if tab_count == 0:
                    folder_len[0] = line_len
                else:
                    folder_len[tab_count] = folder_len[tab_count - 1] + line_len + 1

        return result


s = Solution()
inp = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
res = s.lengthLongestPath(inp)
print(res)
