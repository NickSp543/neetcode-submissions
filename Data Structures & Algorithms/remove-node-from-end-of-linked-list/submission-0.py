# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        if n == count:
            return head.next


        store = head
        for i in range(count - 1 - n):
            head = head.next


        head.next = head.next.next
        return store