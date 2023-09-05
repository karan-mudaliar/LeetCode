# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        curr.next = head

        
        k = k % length
        k = length - k 
        while k > 0 :
            k -= 1
            curr = curr.next
        print(curr.val)
        new_head = curr.next
        curr.next = None
        return new_head

        