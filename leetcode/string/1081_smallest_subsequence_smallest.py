class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndex = {char: i for (i, char) in enumerate(s)}
        stack = []
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue
            while stack and char < stack[-1] and i < lastIndex[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(char)
            seen.add(char)

        return "".join(stack)


s = Solution()
res = s.smallestSubsequence("cbacdcbc")
print(res)
