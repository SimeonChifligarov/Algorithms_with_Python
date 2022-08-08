# def calc_fib(num):
#     if num in [0, 1]:
#         return num
#     return calc_fib(num - 1) + calc_fib(num - 2)


def calc_fib(num, memo):
    if num in memo:
        return memo[num]

    if num in [0, 1]:
        return num

    result = calc_fib(num - 1, memo) + calc_fib(num - 2, memo)
    memo[num] = result
    return result


n = int(input())
print(calc_fib(n, {}))
