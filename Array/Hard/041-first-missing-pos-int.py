def firstMissingPositive(nums):
    # solution1:
    if not nums:
        return 1
    sorted_positive = dict()
    for n in nums:
        if n <= 0:
            continue
        sorted_positive[n] = n
    # print(sorted_positive, len(nums))
    index = 1
    while 1:
        # print(index, sorted_positive.get(index))
        if not sorted_positive.get(index):
            return index
        index += 1

    # solution2:
    # nums = sorted(nums)
    # expected = 1
    # previous = 0
    #
    # # print(nums, expected, previous)
    # for n in nums:
    #     # print(n, expected, previous)
    #     if n <= 0:
    #         continue
    #     # if n != expected and n != previous:
    #     #     return expected
    #     if n != previous:
    #         if n != expected:
    #             return expected
    #         previous = n
    #         expected += 1
    #
    # return expected

    # solution3:
    # nums = sorted(nums)
    #
    # start, i = 1, 1
    # while i < len(nums):
    #     if nums[i] != nums[i - 1]:
    #         nums[start] = nums[i]
    #         start += 1
    #     i += 1
    #
    # expected = 1
    # for num in nums:
    #     if num <= 0:
    #         continue
    #     if num != expected:
    #         return expected
    #     else:
    #         expected += 1
    # return expected

    # solution4:
    # mem = set()
    # max_num = -float("inf")
    # for num in nums:
    #     mem.add(num)
    #     max_num = max(max_num, num)
    #
    # if max_num < 0:
    #     return 1
    #
    # for i in range(1, max_num):
    #     if i not in mem:
    #         return i
    #
    # return max_num + 1


# print(firstMissingPositive([1, 2, 4]))
# print(firstMissingPositive([1, 2, 0]))
# print(firstMissingPositive([3, 4, -1, 1]))
# print(firstMissingPositive([7, 8, 9, 11, 12]))
print(firstMissingPositive([1]))
# print(firstMissingPositive([1, 1, 1, 2, 7]))
