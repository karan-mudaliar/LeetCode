# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_q = self.dfs(root, q, [])
        path_p = self.dfs(root, p, [])
        
        lca = None
        for node_q, node_p in zip(path_q, path_p):
            if node_q == node_p:
                lca = node_q
            else:
                break
        
        return lca
        
    
    def dfs(self,root, target,path = []):

        if root == None:
            return None

        path.append(root)

        if root.val == target.val:
            return path

        left = self.dfs(root.left, target, path.copy())
        if left:
            return left
        
        right = self.dfs(root.right, target, path.copy())
        if right:
            return right

        return None



