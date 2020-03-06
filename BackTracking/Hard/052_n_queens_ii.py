class Solution:
    def totalNQueens(self, n: int) -> int:
        self.counts = 0
        columns = [-1] * n
        self.backtracking(n, 0, columns)
        return self.counts

    def backtracking(self, n, row, columns):
        # 是否在所有n行里都摆放好了皇后？
        if row == n:
            self.counts += 1  # 找到了新的摆放方法
            return
        # 尝试着将皇后放置在当前行中的每一列
        for col in range(0, n):
            columns[row] = col
            # 检查是否合法，如果合法就继续到下一行
            if self.check(row, col, columns):
                self.backtracking(n, row + 1, columns)
            else:
                # 如果不合法，就不要把皇后放在这列中（回溯）
                columns[row] = -1

    def check(self, row, col, columns):
        # print(columns)
        for r in range(row):
            # print(r)
            if columns[r] == col or row - r == abs(columns[r] - col):
                return False

        return True


s = Solution()
n = 2
print(s.totalNQueens(n))
