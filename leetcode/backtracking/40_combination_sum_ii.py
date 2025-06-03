from typing import List, Dict, Tuple
from collections import Counter


class Solution:
	def helper(self, candidates: List[Tuple[int, int]], index: int, target: int) -> List[List[int]]:
		"""
		As we need to make sure every solution is unique we decide first number occurences are
		different in each of them.
		We count occurences of each element and try to iterate over it.
		"""
		if index == len(candidates) or target < 0:
			return []

		(candidate, freq) = candidates[index]
		amount = target
		base_list = []
		result = []
		for i in range(freq + 1):
			if amount < 0:
				break
			if amount == 0:
				result.append(base_list)
				break

			subresults = self.helper(candidates, index + 1, amount)
			for subresult in subresults:
				result.append(base_list + subresult)

			amount -= candidate
			base_list.append(candidate)
		return result

	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		counters: Dict[int, int] = Counter(candidates)
		candidate_counts = [(c, freq) for (c, freq) in counters.items()]
		return self.helper(candidate_counts, 0, target)


s = Solution()
res = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(res)
