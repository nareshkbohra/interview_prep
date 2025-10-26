from typing import List


class Solution:
    def sign(self, n):
        return abs(n) // n

    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()

        for index, num in enumerate(nums):
            if index in visited:
                continue

            currPath = set()
            currIndex = index

            while True:
                if currIndex in currPath:
                    return True

                currNum = nums[currIndex]
                nextIndex = (currIndex + currNum) % len(nums)
                if currIndex == nextIndex:
                    break
                nextNum = nums[nextIndex]
                if self.sign(currNum) != self.sign(nextNum):
                    break

                currPath.add(currIndex)
                currIndex = nextIndex
            visited.add(index)

        return False


s = Solution()
nums = [-2, 1, -1, -2, -2]
res = s.circularArrayLoop(nums)
print(res)
