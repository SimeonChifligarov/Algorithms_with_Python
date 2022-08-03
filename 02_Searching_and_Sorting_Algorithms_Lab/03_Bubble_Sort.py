# Bubble Sort

nums = [int(el) for el in input().split()]

# # bubble sort #1
#
# for i in range(len(nums)):
#     for j in range(1, len(nums) - i):
#         if nums[j - 1] > nums[j]:
#             nums[j], nums[j - 1] = nums[j - 1], nums[j]

# bubble sort #2 => improvement with check "is_sorted"

is_sorted = False
i = 0
while not is_sorted:
    is_sorted = True
    for j in range(1, len(nums) - i):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            is_sorted = False
    i += 1

print(*nums)
