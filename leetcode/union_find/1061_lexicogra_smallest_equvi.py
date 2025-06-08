class Solution:
    def __init__(self):
        self.union = []

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.union = [i for i in range(26)]

        for a, b in zip(s1, s2):
            num1 = ord(a) - ord("a")
            parent1 = self.find(num1)
            num2 = ord(b) - ord("a")
            parent2 = self.find(num2)
            if parent2 > parent1:
                self.union[parent2] = parent1
            else:
                self.union[parent1] = parent2

        result = ""
        for ch in baseStr:
            num = ord(ch) - ord("a")
            result += chr(self.find(num) + ord("a"))

        return result

    def find(self, num):
        if num != self.union[num]:
            return self.find(self.union[num])
        return num


def main():
    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    s = Solution()
    res = s.smallestEquivalentString(s1, s2, baseStr)
    print(res)


main()
