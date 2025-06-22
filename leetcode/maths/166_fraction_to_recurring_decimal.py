class Solution:
    def getFraction(self, nr, dr):
        map = {}
        repeatingNum = float("inf")
        while True:
            if nr == 0:
                break
            # Check if we have seen this number, if yes then it is repeating
            if nr in map:
                repeatingNum = nr
                break
            # We have not seen this number, multiply by 10 and divide by dr.
            # Append the result, new num is remainder
            map[nr] = (nr * 10) // dr
            nr = (nr * 10) % dr

        result = ""
        for key, val in map.items():
            if key == repeatingNum:
                result += "("
            result += str(val)
        if repeatingNum != float("inf"):
            result += ")"
        return result

    def sign(self, n):
        return abs(n) // n

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"
        num = abs(numerator)
        den = abs(denominator)
        result = ""
        if self.sign(numerator) * self.sign(denominator) == -1:
            result += "-"
        result += str(num // den)
        fraction = self.getFraction(num % den, den)

        if fraction:
            result += f".{fraction}"
        return result


s = Solution()
print(s.fractionToDecimal(1, 2))
print(s.fractionToDecimal(2, 1))
print(s.fractionToDecimal(4, 333))
print(s.fractionToDecimal(19, 90))
print(s.fractionToDecimal(-50, 8))
print(s.fractionToDecimal(0, 1))
