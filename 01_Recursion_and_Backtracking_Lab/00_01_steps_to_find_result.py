# Algorithmic Complexity
# Algorithm Analysis
# maximum steps to find the result

def get_operations_count(n):
    counter = 0
    for i in range(n):
        for j in range(n):
            counter += 1
    return counter

# Solution:
# T(n) = 3(n ^ 2) + 3n + 3


# print(get_operations_count(4))
# print(get_operations_count(11))
# print(get_operations_count(1337))
