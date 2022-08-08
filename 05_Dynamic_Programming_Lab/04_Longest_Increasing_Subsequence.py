# # Solution 1
# from collections import deque
#
# nums = [int(el) for el in input().split()]
#
# length = [0] * len(nums)
# parent = [0] * len(nums)
# best_len, best_idx = 0, 0
# for curr_idx in range(len(nums)):
#     curr_num, curr_len, curr_parent = nums[curr_idx], 1, -1
#     for prev_idx in range(curr_idx - 1, -1, -1):
#         prev_number = nums[prev_idx]
#         prev_len = length[prev_idx]
#         if curr_num > prev_number and prev_len + 1 >= curr_len:
#             curr_len = prev_len + 1
#             curr_parent = prev_idx
#     length[curr_idx] = curr_len
#     parent[curr_idx] = curr_parent
#
#     if curr_len > best_len:
#         best_len = curr_len
#         best_idx = curr_idx
#
# lis = deque()
# idx = best_idx
#
# while idx != -1:
#     lis.appendleft(nums[idx])
#     idx = parent[idx]
#
# print(*lis, sep=' ')
#

# Solution 2
from collections import deque

nums = [int(el) for el in input().split()]

size = [0] * len(nums)
size[0] = 1
parent = [None] * len(nums)

best_idx = 0
best_size = 1

for current in range(1, len(nums)):
    current_number = nums[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]

        if prev_number >= current_number:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = current

# print(max(size))

# print(best_size)

# result = []
result = deque()

while best_idx is not None:
    result.appendleft(nums[best_idx])
    best_idx = parent[best_idx]

# print(result[::-1])
print(*result)
