from typing import List


class DSU:
    def __init__(self):
        self.rank = {}
        self.parent = {}
        self.children_count = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            self.children_count[x] = 1
            return x

        if x != self.parent[x]:
            parent = self.find(self.parent[x])
            self.parent[x] = parent

        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return

        rank_x, rank_y = self.rank[x], self.rank[y]
        if rank_x > rank_y:
            self.parent[y] = parent_x
            self.children_count[parent_x] += self.children_count[parent_y]
        elif rank_y > rank_x:
            self.parent[x] = parent_y
            self.children_count[parent_y] += self.children_count[parent_x]
        else:
            self.parent[x] = parent_y
            self.rank[parent_y] += 1
            self.children_count[parent_y] += self.children_count[parent_x]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dsu = DSU()
        num_set = set(nums)
        for num in nums:
            dsu.find(num)
            if num - 1 in num_set:
                dsu.union(num, num - 1)
            if num + 1 in num_set:
                dsu.union(num, num + 1)

        return max(dsu.children_count.values())


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
res = s.longestConsecutive(nums)
print(res)
