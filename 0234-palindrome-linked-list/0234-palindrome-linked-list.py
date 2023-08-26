# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        start = head
        while start is not None:
            stack.append(start.val)
            start = start.next

        start = head

        while start is not None:
            if start.val != stack.pop():
                return False
            start = start.next
        return True