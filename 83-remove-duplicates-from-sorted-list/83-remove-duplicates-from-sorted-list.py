# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head            
        curr = head
        
        if head:
            while curr.next:
                if curr.next.val>prev.val:
                    prev.next=curr.next
                    prev=prev.next
                curr=curr.next
            prev.next=None

        return head