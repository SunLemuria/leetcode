import heapq
import random

# heap / quick sort


# HEAP RUN TIME O(N + klgN)
# min - heap
class Solution1:
    def findKthLargest(self, nums, k) -> int:
        ans = nums[:k]
        heapq.heapify(ans)  # run time O(n)
        for i in range(k, len(nums)):
            heapq.heappushpop(ans, nums[i])  # if nums[i] > ans[0] => heapq.push, run time O(klgn)
        # print(ans)
        return ans[0]


# fastest
# max - heap - #1
class Solution2:
    def findKthLargest(self, nums, k) -> int:
        ans = heapq.nlargest(k, nums)  # run time O(n+klgn)
        return ans[-1]


# max - heap - #2
class Solution3:
    def findKthLargest(self, nums, k) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)  # run time O(k)
        for _ in range(k):
            ans = heapq.heappop(nums)  # run time O(nlgk)
        return -ans


# QUICK SELECT RUN TIME O(N) ON AVERAGE
class Solution4:
    # quick select, based on quick sort
    def findKthLargest(self, nums, k: int) -> int:
        pivot = random.choice(nums)
        # print(nums, k, pivot)
        l, r, m = [], [], []
        for i in nums:
            if i == pivot:
                m.append(i)
            elif i < pivot:
                l.append(i)
            else:
                r.append(i)
        # print(l, m, r)
        ll, lm, lr = len(l), len(m), len(r)
        if lr < k <= lr + lm:
            return m[0]
        elif k <= lr:
            return self.findKthLargest(r, k)
        else:
            return self.findKthLargest(l, k - lr - lm)
