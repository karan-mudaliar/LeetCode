# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            fast = slow = head
            fast = fast.next
            while fast.next and slow.next:
                if fast == slow:
                    return True
                fast = fast.next.next
                slow = slow.next
        except:
            return False
        