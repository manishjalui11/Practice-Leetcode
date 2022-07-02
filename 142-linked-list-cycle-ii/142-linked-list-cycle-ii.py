# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        
        while head:
            if head.next in visited:
                return head.next
            
            visited[head] = True
            head = head.next
            