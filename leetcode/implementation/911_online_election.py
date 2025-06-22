from typing import List, Dict
from collections import defaultdict


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        """
        Approach:
            1. We need to mark when a winner changes and maintain that in a list
            2. We need to maintain a count of all the person.
            3. Know which person is winner right now to compare.
        """
        counter: Dict[int, int] = defaultdict(lambda: 0)
        timeArray = [(persons[0], times[0])]
        counter[persons[0]] = 1
        for person, time in list(zip(persons, times))[1:]:
            counter[person] += 1
            (winPerson, winTime) = timeArray[-1]
            if winPerson == person or counter[person] < counter[winPerson]:
                continue
            timeArray.append((person, time))
        self.timeArray = timeArray

    def q(self, t: int) -> int:
        left, right = 0, len(self.timeArray) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            person, time = self.timeArray[mid]
            if time == t:
                return person
            if time < t:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.timeArray[ans][0]


topCandidates = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
queries = [3, 12, 25, 15, 24, 8]
for q in queries:
    print(topCandidates.q(q))


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
