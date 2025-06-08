class Solution:
    def robotWithString(self, s: str) -> str:
        min_string = ""
        min_char = s[-1]
        for ch in reversed(s):
            min_char = min(min_char, ch)
            min_string = min_char + min_string
        result = ""
        t = ""
        initial_len = len(s)
        for i in range(initial_len):
            if t == "" or (min_string and min_string[0] < t[-1]):
                result += min_string[0]
                index = s.find(min_string[0])
                t += "".join(s[:index])
                s = s[index + 1 :]
                min_string = min_string[index + 1 :]
            else:
                result += t[-1]
                t = t[:-1]

        return result


s = Solution()
res = s.robotWithString("bdda")
print(res)
