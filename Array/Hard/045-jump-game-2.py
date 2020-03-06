def jump(nums):
    ans = 0
    cur = 0
    nex = 0
    for i in range(len(nums)):
        if cur < i:
            cur = nex
            nex = i
            ans += 1
        nex = max(i + nums[i], nex)
    return ans


'''
In each loop we consider the steps s needed to reach the current interval [h, t]. 
We only need to calculate the maximum reach r from [h, t]. Let the new interval to be [t, r],
 and steps of corresponding to the new interval to be s+1. Write the loop to be the following:
'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        h, t, s = 0, 0, 0
        while t < len(nums) - 1:
            h, t, s = t, max([i + nums[i] for i in range(h, t + 1)]), s + 1
        return s


class Solution1:
    def jump(self, nums: List[int]) -> int:
        x = len(nums)
        h = t = 0
        sums = [i + nums[i] for i in range(x)]
        while (t < x - 1):
            m = sums[h]
            for i in range(h, t + 1):
                if m < sums[i]:
                    m = sums[i]
            t = m
            h += 1
        return h


class Solution2:
    def jump(self, nums: List[int]) -> int:
        '''
        this one is faster
        '''
        size = len(nums)

        # destination is last index
        destination = size - 1

        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0

        # counter for jump
        times_of_jump = 0

        # Quick response if start index == destination index == 0
        if size == 1:
            return 0

        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range(0, size):

            # extend current coverage as further as possible
            cur_coverage = max(cur_coverage, i + nums[i])

            # forced to jump (by lazy jump) to extend coverage
            if i == last_jump_index:

                # update last jump index
                last_jump_index = cur_coverage

                # update counter of jump by +1
                times_of_jump += 1

                # check if reached destination already
                if cur_coverage >= destination:
                    return times_of_jump

        return times_of_jump


def jump1(self, nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    jumps = 0
    cur_ladder_end = -1
    next_ladder_end = -1

    for i in range(len(nums)):  # 0, 1
        step_jump = i + nums[i]  # 1, 2
        if cur_ladder_end == -1:
            cur_ladder_end = step_jump  # 1
            jumps += 1  # 1
        else:
            if step_jump > next_ladder_end:  # 2
                next_ladder_end = step_jump  # 2
            if i >= cur_ladder_end and i < len(nums) - 1:  # 1
                cur_ladder_end = next_ladder_end
                jumps += 1

    return jumps


array = [2, 3, 1, 1, 4]
print(jump(array))
