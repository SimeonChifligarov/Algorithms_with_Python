# # Linear search (Solution)
# # for each item in the list:
# #   if that item has the desired value,
# #     return the item's location
# # return nothing
#
# def linear_search(nums, target):
#     for idx, num in enumerate(nums):
#         if num == target:
#             return idx
#     return -1
#
#
# current_nums = [n for n in range(7)]
# current_target = 5
#
# print(linear_search(current_nums, current_target))  # 5
# print(linear_search(current_nums, -10))  # -1


# # Binary Search (Iterative)
# # PURE:
# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid_idx = (left + right) // 2
#         mid_el = nums[mid_idx]
#
#         if mid_el == target:
#             return mid_idx
#
#         if target > mid_el:
#             left = mid_idx + 1
#         else:
#             right = mid_idx - 1
#
#     return -1
#
#
# current_nums = [int(el) for el in input().split()]
# current_target = int(input())
#
# print(binary_search(current_nums, current_target))


# Binary Search (Iterative)
# Problem solution
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if target > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


current_nums = [int(el) for el in input().split()]
current_target = int(input())

result = binary_search(current_nums, current_target)
# print(f'Index of {current_target} is {result}')
print(result)
