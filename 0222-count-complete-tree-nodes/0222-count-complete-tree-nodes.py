# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
            
        count = 0
        node = root
        Q = []
        Q.append(node)
        
        while Q:
            curr = Q.pop(0)
            count += 1
            
            if curr and curr.left is not None:
                Q.append(curr.left)
            if curr and curr.right is not None:
                Q.append(curr.right)
        return count

    