# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        c = 0
        while curr:
            c+=1
            curr = curr.next
        curr = head
        mid=c//2
        while mid:
            mid-=1
            curr = curr.next       
        return curr