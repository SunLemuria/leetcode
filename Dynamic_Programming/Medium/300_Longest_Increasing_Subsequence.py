class DPSolution:
    def __init__(self):
        self.max = 1
        self.cache = dict()

    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        self.f(nums, len(nums))
        return self.max

    def f(self, nums, n):
        if n in self.cache:
            return self.cache[n]
        if n <= 1:
            return n

        result = 0
        max_ending_here = 1

        for i in range(1, n):
            result = self.f(nums, i)
            if nums[i - 1] < nums[n - 1] and result + 1 > max_ending_here:
                max_ending_here = result + 1
        if self.max < max_ending_here:
            self.max = max_ending_here

        self.cache[n] = max_ending_here
        return max_ending_here

    def lengthOfLIS_best(self, nums) -> int:
        if not nums:
            return 0
        L = len(nums)
        dp = [1] * L
        pre_max = nums[0]
        for i in range(1, L):
            pre_max = max(nums[i - 1], pre_max)   # 记录最大值
            for j in range(i - 1, -1, -1):  # 从后往前遍历,利用前面已有的结果
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if nums[j] == pre_max:  # 已经找到前面的最大值, 表示不可能有更长的上升序列了,没必要再往前搜索
                        break
        return max(dp)


class BinarySearchSolution:
    pass


s = DPSolution()
# seq = [10, 9, 2, 5, 3, 7, 101, 18]
seq = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(s.lengthOfLIS_best(seq))
