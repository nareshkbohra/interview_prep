from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.visited = set()
        self.n = 0

    def backtrack(self, current_num: int) -> bool:
        self.path.append(current_num)
        self.visited.add(current_num)

        if len(self.path) == (1 << self.n):
            return True

        for i in range(self.n):
            neighbor = current_num ^ (1 << i)

            if neighbor not in self.visited:
                if self.backtrack(neighbor):
                    return True

        self.path.pop()
        self.visited.remove(current_num)

        return False

    def grayCode(self, n: int) -> List[int]:
        self.path = []
        self.visited = set()
        self.n = n
        self.backtrack(0)

        return self.path


# --- Testing the code ---
s = Solution()
res_3 = s.grayCode(3)
print(f"n=3: {res_3}")  # Expected: [0, 1, 3, 2, 6, 7, 5, 4] or similar

s = Solution()  # Re-instantiate to clear state
res_4 = s.grayCode(4)
print(f"n=4: {res_4}")  # Expected: [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
