from collections import deque

first = input().split()
second = input().split()

rows = len(first) + 1
cols = len(second) + 1

dp = []
# for _ in range(rows):
#     dp.append([0] * cols)
[dp.append([0] * cols) for _ in range(rows)]

# print(dp)

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

result = deque()
row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.appendleft(first[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(*result)
# print(dp[rows - 1][cols - 1])
print(len(result))
