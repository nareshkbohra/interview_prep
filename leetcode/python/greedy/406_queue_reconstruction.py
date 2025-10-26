from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Need to put highest number first
        """
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            result.insert(person[1], person)

        return result
