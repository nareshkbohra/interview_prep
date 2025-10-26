class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = set(["(", "{", "["])
        close_bracket_mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            else:
                open = close_bracket_mapping[ch]
                if len(stack) == 0:
                    return False
                if stack[-1] != open:
                    return False
                stack.pop()

        return len(stack) == 0
