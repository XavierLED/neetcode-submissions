# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        left = 0
        while l1 or l2 or left:
            var1 = l1.val if l1 else 0
            var2 = l2.val if l2 else 0

            cur.next = ListNode((var1 + var2 + left) % 10)
            left = (var1 + var2 + left) // 10
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


            
