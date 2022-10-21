# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return TreeNode(nums[0])
        
        def helper(array, root,left,right):
            if right<left:
                return
            mid = (right+left)//2
            val = nums[mid]
            
            new_node =TreeNode(val)
            
            if root == None:
                root = new_node
            
            elif val < root.val:
                root.left = new_node
                root = root.left
            else:
                root.right = new_node
                root = root.right
            
            helper(array,root,left,mid-1)
            helper(array,root,mid+1,right)
            return root
        
        return helper(nums,None,0,len(nums)-1)
            
        
        