class SegmentTreeNode:
    # slowest
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.cnt = 0


class Solution:
    def _build(self, left, right):
        root = SegmentTreeNode(self.nums[left], self.nums[right])
        if left == right:
            return root

        mid = (left + right) // 2
        root.left = self._build(left, mid)
        root.right = self._build(mid + 1, right)
        return root

    def _update(self, root, val):
        if not root:
            return
        if root.low <= val <= root.high:
            root.cnt += 1
            self._update(root.left, val)
            self._update(root.right, val)

    def _query(self, root, lower, upper):
        if lower <= root.low and root.high <= upper:
            return root.cnt
        if upper < root.low or root.high < lower:
            return 0
        return self._query(root.left, lower, upper) + self._query(root.right, lower, upper)

    # O(nlogn)
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        self.nums = sorted(list(set(nums)))
        root = self._build(0, len(self.nums) - 1) if nums else None

        res = []
        for n in nums:
            res.append(self._query(root, float('-inf'), n - 1))
            self._update(root, n)
        return res[::-1]


class SolutionBisect:
    # First place
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76637/6-line-python-solution-using-bisect
    def countSmaller(self, nums):
        import bisect
        counts, sortednums = [], []
        # iterate backwards
        for i in range(len(nums)-1,-1, -1):
            # would be inserted in the LEFT position
            position = bisect.bisect_left(sortednums, nums[i])
            # binary insert to keep sorted order
            sortednums.insert(position, nums[i])
            counts.append(position)
        return counts[::-1]


class SolutionBinaryIndexedTree:
    # second place
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76731/Nlogn-Python-solution-binary-indexed-tree-160-ms
    def countSmaller(self, nums):
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]