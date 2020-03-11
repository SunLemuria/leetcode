class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        dp = [1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]


s = Solution()
neigh = [1, 2, 3, 1]
print(s.rob(neigh))
