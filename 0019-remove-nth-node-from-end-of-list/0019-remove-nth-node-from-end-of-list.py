# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     

        fast = slow = head
        count = n
        while count > 0:
            count -= 1
            fast = fast.next
        
        if not fast:
            return head.next

        print(fast.val)

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head