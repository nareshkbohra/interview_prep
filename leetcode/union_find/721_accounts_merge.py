from typing import List, Dict
from collections import defaultdict


class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, n):
        if n not in self.parent:
            self.parent[n] = n
            self.rank[n] = 1
            return n

        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[parent_y] = parent_x
        elif self.rank[y] > self.rank[x]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccIdMap = {}
        dsu = DSU()
        for index, account in enumerate(accounts):
            email_ids = account[1:]
            for email in email_ids:
                if email not in emailToAccIdMap:
                    emailToAccIdMap[email] = index
                dsu.union(emailToAccIdMap[email], dsu.find(index))

        result: Dict[int, List[str]] = defaultdict(list)
        for i in range(len(accounts)):
            result[dsu.find(i)].extend(accounts[i][1:])
        accMapping = []
        for idx, emails in result.items():
            curr_result = [accounts[idx][0]]
            curr_result.extend(sorted(set(emails)))
            accMapping.append(curr_result)
        return accMapping


accs = [
    ["David", "David0@m.co", "David4@m.co", "David3@m.co"],
    ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
    ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
    ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
    ["David", "David4@m.co", "David1@m.co", "David3@m.co"],
]
s = Solution()
res = s.accountsMerge(accs)
print(res)
