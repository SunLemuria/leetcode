class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        prev = None
        result = list()

        for curr in intervals:
            if prev is None or curr[0] > prev[1]:
                result.append(curr)
                prev = curr
            else:
                # 改变了原数组
                prev[1] = max(prev[1], curr[1])

        return result


s = Solution()
intervals = [[0, 6], [1, 5], [7, 8], [8, 10]]
print(s.merge2(intervals))
