# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/basic-calculator-iii.py

# Time:  O(n)
# Space: O(n)


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)


class Solution2(object):
    def calculate(self, s):
        queue = list()
        for ch in s:
            if ch != ' ':
                queue.append(ch)
        queue.append('+')

        return self.compute(queue)

    def compute(self, queue):

        sign = '+'
        num = 0

        dot = 0
        stack = []
        while queue:
            c = queue.pop(0)
            if c.isdigit():
                if dot:  # 前面已经出现了小数点
                    num = num + int(c) * 10 ** (-dot)  # dot 表示当前c应该在小数点后多少位
                else:
                    num = 10 * num + int(c)

            elif c == '.':
                dot += 1
                continue
            elif c == "(":
                # 遇到一个左括号，开始递归调用，求得括号里的计算结果，将它赋给当前的 num
                num = self.compute(queue)
                dot = 0
            else:
                dot = 0
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] /= num
                num = 0
                sign = c
                # 遇到右括号，就可以结束循环，直接返回当前的总和
                if sign == ")":
                    break

        return sum(stack)


s = '1 + (10.10/ 2) * 2-999'
# s = '(91/ 2)'
# s = '1+ (10/ 2)'
so = Solution2()
print(so.calculate(s))
