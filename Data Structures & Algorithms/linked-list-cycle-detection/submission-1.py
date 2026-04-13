# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        currentNode = head
        fast_pt = currentNode
        slow_pt = currentNode
        while fast_pt.next:
            if not fast_pt.next.next:
                return False
            fast_pt = fast_pt.next.next
            slow_pt = slow_pt.next
            if fast_pt==slow_pt:
                return True
        return False
        