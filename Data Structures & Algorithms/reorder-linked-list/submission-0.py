class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # count n
        temp = head
        size = 0

        while temp:
            temp = temp.next
            size += 1

        # find the end of the first half
        first_tail = head

        for i in range(math.ceil(size / 2) - 1):
            first_tail = first_tail.next

        second_head = first_tail.next
        first_tail.next = None

        # reverse second half
        prev = None
        curr = second_head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        # IMPORTANT
        second_head = prev

        # merge
        while second_head:
            temp1 = head.next
            temp2 = second_head.next

            head.next = second_head
            second_head.next = temp1

            head = temp1
            second_head = temp2