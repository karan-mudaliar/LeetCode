# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            root = TreeNode(val = val)
            return root
        curr = root
        while True:
            if val < curr.val:
                if curr.left == None:
                    curr.left = TreeNode(val = val)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.right = TreeNode(val = val)
                    break
                else:
                    curr = curr.right
        return root
                
                