# iterative solution is better;
# but recursion practice is goal here;

def array_sum(nums, idx):
    if idx == len(nums) - 1:  # base case
        return nums[idx]
    # print(idx)
    return nums[idx] + array_sum(nums, idx + 1)  # recursive call


numbers = [int(el) for el in input().split()]

print(array_sum(numbers, 0))
