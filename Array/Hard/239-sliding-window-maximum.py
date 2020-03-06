def maxSlidingWindow(nums, k):
    from collections import deque
    d, answer = deque([]), []
    for i in range(len(nums)):
        if d and d[0] <= i - k:
            d.popleft()
        while d and nums[d[-1]] < nums[i]:
            d.pop()
        d.append(i)
        if i >= k - 1:
            answer.append(nums[d[0]])
    return answer

    # begin = 0
    # q = deque([])
    # output = []
    # for end in range(len(nums)):
    #     #######
    #     # This make sures that the leftmost element must be the largest
    #     # Note that we are not adding the element but its index
    #     while q and nums[end] > nums[q[-1]]:
    #         q.pop()
    #
    #     # This makes sure every element will be added into queue
    #     q.append(end)
    #
    #     # This makes sure that for every sliding window
    #     # the leftmost element will be removed from the queue
    #     # if it is not within the sliding window
    #     while end - begin + 1 > k:
    #         begin += 1
    #         if q[0] < begin:
    #             q.popleft()
    #
    #         # for every sliding window
    #         # we add the leftmost element (maxium within the sliding window) into the output
    #     if end - begin + 1 == k:
    #         output.append(nums[q[0]])
    #
    # return output
