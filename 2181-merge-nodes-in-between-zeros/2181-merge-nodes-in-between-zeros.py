# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        prev = start
        node = head.next
        while node:
            temp = 0
            while node.val != 0:
                temp += node.val
                node = node.next
            if temp > 0:
                start.val = temp
                prev = start
                start.next = node
                start = node
            node = node.next
        prev.next = None
        return head