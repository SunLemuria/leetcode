def twoSum(nums, target):
    # # 偶数
    # is_even = not target % 2
    # half = int(target / 2)
    # if is_even:
    #     even_indexes = list()
    #     for i, n in enumerate(nums):
    #         if n == half:
    #             even_indexes.append(i)
    #     if len(even_indexes) >= 2:  # 如果有超过2个数正好为一半,返回前两个的下标
    #         return even_indexes[:2]
    #
    # # 奇数或target的一半少于2个:
    # for i, n in enumerate(nums):
    #     if target - n in nums:
    #         j = nums.index(target - n)
    #         if j != i:
    #             return [i, j]
    h = {}
    for i, num in enumerate(nums):
        # n = target - num
        # if n not in h:
        #     h[num] = i
        # else:
        #     return [h[n], i]

        if target - num in h:
            return [h[target - num], i]
        h[num] = i


array = [3, 3]
indexes = twoSum(array, 6)
print(indexes)
