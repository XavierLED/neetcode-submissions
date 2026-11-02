# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSameTree(self, root, subRoot):
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.right, subRoot.right) and self.isSameTree(root.left, subRoot.left)
        elif not root and not subRoot:
            return True
        return False
        

