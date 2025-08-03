from typing import List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        num_candidates = len(votes[0])
        scores = {}
        for vote in votes[0]:
            scores[vote] = [0] * num_candidates
            scores[vote].append(-ord(vote))
        for vote in votes:
            for rank, candidate in enumerate(vote):
                scores[candidate][rank] += 1
        scores = sorted(scores.values(), reverse=True)
        print(scores)
        return "".join(chr(-score[-1]) for score in scores)


s = Solution()
votes = ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]
res = s.rankTeams(votes)
print(res)
