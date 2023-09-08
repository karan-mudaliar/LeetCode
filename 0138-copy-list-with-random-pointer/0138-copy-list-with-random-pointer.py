"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        H = {None : None}

        curr = head
        while curr:
            H[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = H[curr]
            copy.next, copy.random = H[curr.next], H[curr.random]
            curr = curr.next

        return H[head]