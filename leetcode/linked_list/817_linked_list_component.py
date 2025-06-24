from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        result = 0
        numsSet = set(nums)
        while head:
            if head.val not in numsSet:
                head = head.next
                continue
            result += 1
            while head.val in nums:
                head = head.next
        return result
