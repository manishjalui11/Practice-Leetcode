# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        len1=self.len(headA)
        len2=self.len(headB)
        res = len1-len2
        
        if res>0:
            while res:
                headA=headA.next
                res-=1
                
        elif res<0:
            while res:
                headB=headB.next
                res+=1
        
        while headA and headB:
            if headA==headB:
                return headA 
            else:
                headA=headA.next
                headB=headB.next
        
        return None
        
    def len(self, head: Optional[ListNode]) -> Optional[int]:
        curr = head
        c = 0
        while curr:
            c+=1
            curr = curr.next
        return c
        