from typing import List


class Solution:
    def helper(self, candidates, index, target):
        if len(candidates) == index or target <= 0:
            return []

        result = []
        first_number = candidates[index]
        amount = target
        base_list = []
        while True:
            if amount < 0:
                break
            if amount == 0:
                result.append(base_list)
                break
            sub_results = self.helper(candidates, index + 1, amount)
            for sub_result in sub_results:
                result.append(base_list + sub_result)

            base_list.append(first_number)
            amount -= first_number

        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        First decide frequency of first number then calculate remaining number
        Append both
        """
        return self.helper(candidates, 0, target)


s = Solution()
res = s.combinationSum([2, 3, 5], 8)
print(res)
