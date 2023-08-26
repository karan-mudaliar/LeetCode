# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        start = head

        while start is not None:
            stack.append(start.val)
            start = start.next
        start = head

        while start is not None:
            start.val = stack.pop()
            start = start.next

        return head