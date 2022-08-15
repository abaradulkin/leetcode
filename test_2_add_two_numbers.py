from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        mem = 0
        while l1 or l2 or mem:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            current_sum = val_1 + val_2 + mem
            mem = current_sum // 10
            current_sum = current_sum % 10
            current.next = ListNode(current_sum)

            current = current.next
            l1 = l1.next if type(l1) == ListNode else None
            l2 = l2.next if type(l2) == ListNode else None
        return result.next
