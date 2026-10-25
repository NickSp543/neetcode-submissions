# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None


        dummy = ListNode(0)
        head = dummy

        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
                
            if l2:
                val += l2.val
                l2 = l2.next

            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            head.next = ListNode(val)
            head = head.next
        return dummy.next

