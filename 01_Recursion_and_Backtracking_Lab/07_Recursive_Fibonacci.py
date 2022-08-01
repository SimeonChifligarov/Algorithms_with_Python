# incorrectly used recursion
# USE MEMOIZATION

# def calc_fib(number):
#     if number <= 1:
#         return 1
#     return calc_fib(number - 1) + calc_fib(number - 2)
#
#
# print(calc_fib(int(input())))

# print(calc_fib(10))  # 89
# print(calc_fib(50))  # This will hang!

# # iterative approach - correct!
#
def iterative_fib(number):
    fib_0 = 1
    fib_1 = 1
    if number == 0:
        return fib_0
    if number == 1:
        return fib_1

    result = 0
    for _ in range(number - 1):
        result = fib_0 + fib_1
        fib_0, fib_1 = fib_1, result
    return result


print(iterative_fib(int(input())))

#
# print(iterative_fib(10))
# print(iterative_fib(50))
# print(iterative_fib(0))
# print(iterative_fib(1))
# print(iterative_fib(2))
