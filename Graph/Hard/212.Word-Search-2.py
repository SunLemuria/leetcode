class Solution:
    def findWords(self, words):
        if not board or not words:
            return []

        self.build_trie(words)
        self.result = set()
        self.board = board
        self.m = len(board)
        self.n = len(board[0])

        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                self.dfs(r, c, self.trie)

        return list(self.result)

    def build_trie(self, words):
        self.trie = {}
        for word in words:
            curr_pos = self.trie
            for ch in word:
                if ch not in curr_pos:
                    curr_pos[ch] = {}
                curr_pos = curr_pos[ch]
            curr_pos['isWord'] = word

    def dfs(self, row, col, pos):
        ch = self.board[row][col]

        if ch not in pos:
            return

        pos = pos[ch]
        if 'isWord' in pos:
            self.result.add(pos['isWord'])

        self.board[row][col] = -1
        for cr, cc in self.getNeighbours(row, col, pos):
            self.dfs(cr, cc, pos)
        self.board[row][col] = ch

    def getNeighbours(self, row, col, pos):
        valid = []
        # UP
        if row > 0 and self.board[row - 1][col] in pos:
            valid.append((row - 1, col))
        # DOWN
        if row < self.m - 1 and self.board[row + 1][col] in pos:
            valid.append((row + 1, col))
        # LEFT
        if col > 0 and self.board[row][col - 1] in pos:
            valid.append((row, col - 1))
        # RIGHT
        if col < self.n - 1 and self.board[row][col + 1] in pos:
            valid.append((row, col + 1))

        return valid


class Solution2:
    def findWords(self, board, words):
        if not board or not words:
            return []

        m = len(board)
        n = len(board[0])

        trie = {}

        # 用字典构建前缀树
        for w in words:
            temp_trie = trie
            for c in w:
                if c not in temp_trie:
                    temp_trie[c] = {}
                temp_trie = temp_trie[c]
            temp_trie['\n'] = w

        def search(tree, i, j):
            # 沿着图遍历
            ch = board[i][j]
            temp = tree[ch]
            board[i][j] = ''  # 已遍历的位置不能重复访问, 暂置为空
            if '\n' in temp:   # 字典树已访问到最后,一个完整单词已完结
                self.ans.append(temp.pop('\n'))

            # board下标移动且移动后的字母也在trie树的下一级中,可进行下一次递归调用
            if i > 0 and board[i - 1][j] in temp:
                search(temp, i - 1, j)
            if j > 0 and board[i][j - 1] in temp:
                search(temp, i, j - 1)
            if i < m - 1 and board[i + 1][j] in temp:
                search(temp, i + 1, j)
            if j < n - 1 and board[i][j + 1] in temp:
                search(temp, i, j + 1)

            board[i][j] = ch

        self.ans = []
        # print('trie: \n', trie)
        for a in range(m):
            for b in range(n):
                if board[a][b] in trie:  # trie 中有以此字母开头的单词才开始搜索
                    search(trie, a, b)

        return self.ans


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]
s = Solution2()
print(s.findWords(board, words))
