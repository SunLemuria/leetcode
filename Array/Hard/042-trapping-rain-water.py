import time
import random


def trap(height):
    areas = 0
    max_l = max_r = 0
    l = 0
    r = len(height) - 1
    while l < r:
        if height[l] < height[r]:   # 左低右高,移动左指针
            if height[l] > max_l:
                max_l = height[l]
            else:
                areas += max_l - height[l]
            l += 1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                areas += max_r - height[r]
            r -= 1   # 右低左高,移动右指针
    return areas


# def trap(height):
#     trap_rain = 0
#     # minimum = min(height)
#     # height = [h - minimum for h in height]
#     start = time.time()
#     # print('start, ', start)
#     while any(height):
#         trap_rain += find_trap_zeros(height)
#         for i in range(len(height)):
#             if height[i] != 0:
#                 height[i] -= 1
#     # print('end, ', time.time() - start)
#     return trap_rain
#
#
# def find_trap_zeros(height):
#
#     tail_zero_count = 0
#     total_zero_count = 0
#
#     head_zero_list = list()
#     non_zero_visited = False  # whether a non-zero number is visited
#
#     for i, h in enumerate(height):
#         if not h:
#             total_zero_count += 1
#             tail_zero_count += 1
#             if not non_zero_visited and not any(head_zero_list):  # it's zero at the head
#                 head_zero_list.append(h)
#         else:
#             tail_zero_count = 0
#             non_zero_visited = True
#     return total_zero_count - len(head_zero_list) - tail_zero_count

a = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 2, 1]
# a = [random.randint(0, 10000) for _ in range(10000)]
# a = [1, 0, 1]
# a = [2, 1, 0, 9, 10, 0, 11]
print(trap(a))
