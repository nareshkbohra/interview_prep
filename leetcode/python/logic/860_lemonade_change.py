from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_rupee_notes = 0
        ten_rupee_notes = 0
        for bill in bills:
            if bill == 5:
                five_rupee_notes += 1
                continue

            if bill == 10:
                if five_rupee_notes == 0:
                    return False
                ten_rupee_notes += 1
                five_rupee_notes -= 1
            else:
                if ten_rupee_notes == 0:
                    if five_rupee_notes < 3:
                        return False
                    five_rupee_notes -= 3
                else:
                    if five_rupee_notes == 0:
                        return False
                    ten_rupee_notes -= 1
                    five_rupee_notes -= 1
        return True
