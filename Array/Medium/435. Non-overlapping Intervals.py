class Solution:
    # TLE, violence
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[0])
        return self.erase_overlap_intervals(-1, 0, intervals)

    def erase_overlap_intervals(self, prev, curr, intervals):
        if curr == len(intervals):
            return 0

        taken = 10000000

        if prev == -1 or intervals[prev][1] <= intervals[curr][0]:
            taken = self.erase_overlap_intervals(curr, curr + 1, intervals)

        not_taken = self.erase_overlap_intervals(prev, curr + 1, intervals) + 1
        return min(taken, not_taken)


class Solution2:
    # greedy
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        # 开始时间排序
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]    # 第一个区间结束点
        count = 0  # 目前删除的区间数
        # 从第二个区间开始,判断当前区间与前一个区间的结束位置
        for i in range(1, len(intervals)):
            # 当前区间和前一个区间有重叠，即当前区间的起始时间小于上一个区间的结束时间，
            # end记录下两个结束时间的最小值，把结束时间晚的区间删除，计数加1。
            if intervals[i][0] < end:
                end = min(end, intervals[i][1])
                count += 1
            else:
                end = intervals[i][1]
        # 果没有发生重叠，根据贪婪法，更新 end 变量为当前区间的结束时间
        return count


class Solution3:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        # 结束时间排序
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]  # 第一个区间结束点
        count = 1  # 目前未重复的区间数
        # 从第二个区间开始,判断当前区间与前一个区间的结束位置
        for i in range(1, len(intervals)):
            # 当前区间和前一个结束时间没有重叠，那么计数加 1，同时更新一下新的结束时间
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return len(intervals) - count


intervals = [[1, 2], [1, 2], [1, 2]]
s = Solution3()
c = s.eraseOverlapIntervals(intervals)
print(c)
