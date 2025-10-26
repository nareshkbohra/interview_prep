class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                if len(stack) >= 1 and stack[-1].isdigit():
                    stack[-1] = str(int(stack[-1]) * 10 + int(ch))
                else:
                    stack.append(ch)
                continue

            if ch == "]":
                curr_string = ""
                while True:
                    curr_ch = stack.pop()
                    if curr_ch == "[":
                        break
                    curr_string = curr_ch + curr_string
                num = int(stack.pop())
                stack.append(curr_string * num)
                continue
            stack.append(ch)

        return "".join(stack)


inp = "100[leetcode]"
s = Solution()
res = s.decodeString(inp)
print(res)
