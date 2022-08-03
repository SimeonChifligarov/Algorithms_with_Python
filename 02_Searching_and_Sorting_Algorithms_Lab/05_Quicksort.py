# Quicksort

def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot, left, right = start, start + 1, end
    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1
    nums[pivot], nums[right] = nums[right], nums[pivot]
    quick_sort(nums, start, right - 1)
    quick_sort(nums, right + 1, end)


current_nums = [int(el) for el in input().split()]

quick_sort(current_nums, 0, len(current_nums) - 1)

print(*current_nums)
