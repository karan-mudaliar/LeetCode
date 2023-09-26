# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        # Move prev and curr to the nodes just before left and at left
        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        # Reverse the sublist between left and right
        sublist_head, sublist_tail = prev, curr
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Connect the reversed sublist back to the main list
        sublist_head.next = prev
        sublist_tail.next = curr

        return dummy.next
