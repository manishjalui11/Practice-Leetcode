# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None: return [] 
        queue = [root]
        res=[]
        while (len(queue)>0):
            lvl=[]
            for _ in range(len(queue)):
                curr=queue.pop(0)
                lvl.append(curr.val)
                if curr.left : queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            res.append(lvl)
        return res
        