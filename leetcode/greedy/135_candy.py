from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        no_of_kids = len(ratings)
        candies = [1] * no_of_kids
        for i in range(1, no_of_kids):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(no_of_kids - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


s = Solution()
res = s.candy([1, 0, 2])
print(res)
