# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Symmetric(l,r):
            if l and r:
                if l.val==r.val:
                    return Symmetric(l.left,r.right) and Symmetric(l.right,r.left)
                else:
                    return False
            elif not (l or r): return True
    
        return Symmetric(root.left, root.right)