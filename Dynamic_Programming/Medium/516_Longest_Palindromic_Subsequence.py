class Solution:
    # very slow
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # 定义 dp 矩阵，dp[i][j] 表示从字符串第 i 个字符到第 j 个字符之间的最长回文
        dp = [[0] * n for _ in range(n)]
        # 初始化 dp 矩阵，将对角线元素设为 1，即单个字符的回文长度为 1
        for i in range(n):
            dp[i][i] = 1
        # 从长度为 2 开始，尝试将区间扩大，一直扩大到 n
        for length in range(2, n + 1):
            # 在扩大的过程中，每次都得出区间的其实位置i和结束位置j
            for i in range(0, n - length + 1):
                j = i + length - 1
                # 比较一下区间首尾的字符是否相等，如果相等，就加2；如果不等，从规模更小的字符串中得出最长的回文长度
                if s[i] == s[j]:
                    dp[i][j] = 2 + (0 if length == 2 else dp[i + 1][j - 1])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

    def longestPalindromeSubseq_best(self, s: str) -> int:
        def recur(s, st, end, dp):
            if dp[st][end] is not None:
                return dp[st][end]
            if st > end:
                return 0
            if st == end:
                return 1
            if s[st] == s[end]:
                dp[st][end] = recur(s, st + 1, end - 1, dp) + 2
            else:
                dp[st][end] = max(recur(s, st + 1, end, dp), recur(s, st, end - 1, dp))
            return dp[st][end]

        if not s:
            return 0
        length = len(s)
        dp = [[None] * length for _ in range(length)]
        return recur(s, 0, length - 1, dp)


s = Solution()
string = 'bbbab'
print(s.longestPalindromeSubseq(string))
