# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        lst = []
        currentNode = head.next
        while currentNode!=None:
            lst.append(currentNode.val)
            currentNode = currentNode.next
        i = 0
        j = len(lst)-1
        currentNode = head
        while i<j:
            node_1 = ListNode(lst[j])
            node_2 = ListNode(lst[i])
            currentNode.next = node_1
            currentNode = currentNode.next
            currentNode.next = node_2
            currentNode = currentNode.next
            i+=1
            j-=1
        if i==j:
            currentNode.next = ListNode(lst[i])
        

        
        