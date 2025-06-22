from typing import List, Dict
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Base idea is that we need to start filling a group from smallest number
        possible. So as first number is decided, try to find subsequent numbers, if they are available
        then use them and reduce their count.
        """
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count: Dict[int, int] = Counter(hand)
        for card in hand:
            if count[card] == 0:
                continue
            for i in range(groupSize):
                if count[card + i] == 0:
                    return False
                count[card + i] -= 1

        return True
