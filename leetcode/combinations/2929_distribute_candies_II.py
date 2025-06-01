class Solution:
	def distributeCandies(self, n: int, limit: int) -> int:
		# First give first kid candy, but minimum candy it can have depends
		# on max candy other can have (2l).
		min_candy_first = max(0, n - 2 * limit)
		result = 0
		for i in range(min_candy_first, min(n, limit) + 1):
			remaining_candies = n - i
			# Now next guy can have candies, minimum candies he can have is when
			# next guy does not cross its limit
			min_candy_second = max(0, remaining_candies - limit)
			for _ in range(min_candy_second, min(remaining_candies, limit) + 1):
				result += 1
		return result


s = Solution()
res = s.distributeCandies(3, 3)
print(res)
