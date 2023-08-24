# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        new_head = new = ListNode(0)
        while carry or l1 or l2:
            val1 = l1.val if l1 is not None else 0
            l1 = l1.next if l1 is not None else None
            val2 = l2.val if l2 is not None else 0
            l2 = l2.next if l2 is not None else None

            new_val = (val1 + val2 + carry)
            carry = new_val // 10
            new.next = ListNode(new_val%10)
            new = new.next

        return new_head.next
        