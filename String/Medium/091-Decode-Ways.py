# recursion
class Solution1:
    # TimeLimitExceeded
    def numDecodings(self, s: str) -> int:
        chars = list(s)
        if chars[0] == '0':
            # 以0开头即非法
            return 0
        return self.decode(chars, len(chars) - 1)

    def decode(self, chars, index):
        if index <= 0:
            return 1

        count = 0

        curr = chars[index]
        prev = chars[index - 1]

        if curr > '0':
            # 单个字符,大于0
            count = self.decode(chars, index - 1)

        if prev == '1' or (prev == '2' and curr <= '6'):
            # 两个字符,在1*和26之间
            count += self.decode(chars, index - 2)

        return count

# dynamic programming
