# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #dfs for sure\
        d = 0
        def dfs(root):
            nonlocal d
            if not root:
                return 0
            
            heightR = dfs(root.right)
            heightL = dfs(root.left)
            d = max(d, heightL + heightR)
            return 1 + max(heightL, heightR)
        
        dfs(root)
        return d
