# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # https://leetcode.com/problems/insertion-sort-list/discuss/46470/Concise-python-solution-with-comments
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val:  # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val:  # classic insertion sort to find position
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next  # insert
        return dummy.next

    def best_way(self, head: ListNode) -> ListNode:
        # https://leetcode.com/problems/insertion-sort-list/discuss/46432/AC-Python-192ms-solution
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next
