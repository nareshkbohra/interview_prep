from typing import List


class Solution:
	def __init__(self):
		self.memory = {}

	def generateParenthesis(self, n: int) -> List[str]:
		if n == 0:
			return [""]
		if n == 1:
			return ["()"]
		if n in self.memory:
			return self.memory[n]

		result = []
		for i in range(n):
			inner_results = self.generateParenthesis(i)
			outer_results = self.generateParenthesis(n - 1 - i)
			for inner in inner_results:
				for outer in outer_results:
					result.append("(" + inner + ")" + outer)
		self.memory[n] = result
		return result


s = Solution()
res = s.generateParenthesis(3)
print(res)
