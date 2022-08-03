# Selection Sort

nums = [int(el) for el in input().split()]

for idx in range(len(nums)):
    min_idx = idx
    for curr_idx in range(idx + 1, len(nums)):
        if nums[curr_idx] < nums[min_idx]:
            min_idx = curr_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(*nums)
