import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        # ListNode的比较方法,在heapify时会用到
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        min_heap = [(item.val, item) for item in lists]  # list of head nodes
        heapq.heapify(min_heap)  # a min heap of head nodes
        fake_node = ListNode(None)
        curr_node = fake_node   # curr_node记录合并链表的尾节点
        while min_heap:
            _, next_node = heapq.heappop(min_heap)
            curr_node.next = next_node
            curr_node = curr_node.next
            if next_node.next:  # update min heap
                node_to_push = next_node.next
                heapq.heappush(min_heap, (node_to_push.val, node_to_push))
        return fake_node.next


class Solution2:
    def mergeKLists(self, lists) -> ListNode:
        low = 0
        high = len(lists) - 1
        if high < 0:
            node = ListNode(None)
            return node.next
        return self.merge_k_lists(lists, low, high)

    def merge_k_lists(self, lists, low, high):

        if low == high:
            return lists[low]

        middle = low + int((high - low) / 2)

        return self.mergeTwoLists(
            self.merge_k_lists(lists, low, middle),
            self.merge_k_lists(lists, middle + 1, high)
        )

    def mergeTwoLists(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.val <= b.val:
            a.next = self.mergeTwoLists(a.next, b)
            return a

        b.next = self.mergeTwoLists(a, b.next)

        return b


class Solution3:
    def mergeKLists(self, lists) -> ListNode:

        heap = []
        count = 0

        for i in lists:
            if i:
                # value相同时用count排序
                heap.append((i.val, count, i))
            count += 1
        heapq.heapify(heap)
        head = curr = ListNode(-1)

        while len(heap) > 0:
            _, _, n = heapq.heappop(heap)
            if n.next:
                count += 1
                heapq.heappush(heap, (n.next.val, count, n.next))
            curr.next = n
            curr = n
        return head.next


a = [29, 43, 99]
b = [30, 46, 1000]
c = [25, 36, 87]


head_a = ListNode(a[0])
curr = head_a
for i in range(1, len(a)):
    curr.next = ListNode(a[i])
    curr = curr.next

head_b = ListNode(b[0])
curr = head_b
for i in range(1, len(b)):
    curr.next = ListNode(b[i])
    curr = curr.next

head_c = ListNode(c[0])
curr = head_c
for i in range(1, len(c)):
    curr.next = ListNode(c[i])
    curr = curr.next

# s = Solution()
# head = s.mergeKLists([head_a, head_b, head_c])
# curr = head
# while curr:
#     print(curr.val)
#     curr = curr.next


# s2 = Solution2()
s3 = Solution3()
lists = [head_a, head_b, head_c]
# lists = []
head2 = s3.mergeKLists(lists)
curr = head2
while curr:
    print(curr.val)
    curr = curr.next
