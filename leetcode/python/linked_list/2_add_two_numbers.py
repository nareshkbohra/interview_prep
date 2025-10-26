from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        currNode = head
        carry = 0
        while True:
            if carry == 0 and l1 is None and l2 is None:
                break
            curr_sum = carry
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            carry = curr_sum // 10
            curr_sum = curr_sum % 10
            currNode.next = ListNode(curr_sum)
            currNode = currNode.next

        return head.next
