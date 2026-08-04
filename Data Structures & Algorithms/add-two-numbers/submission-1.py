# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst_1 = []
        lst_2 = []
        cur_node = l1
        while cur_node:
            lst_1.append(str(cur_node.val))
            cur_node = cur_node.next
        cur_node = l2
        while cur_node:
            lst_2.append(str(cur_node.val))
            cur_node = cur_node.next

        num_1 = int("".join(lst_1)[::-1])
        num_2 = int("".join(lst_2)[::-1])
        sum_num = num_1+num_2
        res_str = str(sum_num)[::-1]

        dummy = ListNode()
        cur = dummy
        for s in res_str:
            cur.next = ListNode(int(s))
            cur = cur.next
        return dummy.next
        
        
