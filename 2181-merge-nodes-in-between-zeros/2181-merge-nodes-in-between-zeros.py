# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr and curr.next:
            if curr.next.val!=0:
                curr.val+=curr.next.val
                curr.next=curr.next.next
            else:
                if curr.next.next is None:
                    curr.next=None
                    break
                curr=curr.next
        return head