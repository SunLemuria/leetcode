# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        n = 0
        while head:
            n += 1
            head = head.next

        n = n // k * k

        prev = dummy
        node = dummy.next

        while n > 0:
            i = k
            while i > 1:
                tmp = node.next
                node.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
                i -= 1
                n -= 1
            prev = node
            node = node.next
            n -= 1

        return dummy.next
