# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        currentNode = head
        while currentNode:
            sz += 1
            currentNode = currentNode.next
        if sz==1 and n==1:
            return None
        rmv_num = sz-n
        if rmv_num==0:
            head = head.next
            return head
        i = 0
        currentNode = head
        while i<rmv_num-1:
            currentNode = currentNode.next
            i+=1
        currentNode.next = currentNode.next.next
        return head

        