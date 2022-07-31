# iterative solution is better;
# but recursion practice is goal here;

def calc_factorial(n):
    # if n <= 1:  # bad optimization attempt
    if n == 0:  # base case
        return 1
    return n * calc_factorial(n - 1)  # recursive call


num = int(input())

print(calc_factorial(num))
