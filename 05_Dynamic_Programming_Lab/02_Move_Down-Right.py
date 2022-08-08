# # Solution 1
# from collections import deque
#
# rows = int(input())
# cols = int(input())
#
# matrix = []
# dp = []
# for r in range(rows):
#     matrix.append([int(el) for el in input().split()])
#     dp.append([0] * len(matrix[r]))
#
# # First, find all base solutions
# dp[0][0] = matrix[0][0]
# for row in range(1, rows):
#     dp[row][0] = dp[row - 1][0] + matrix[row][0]
# for col in range(1, cols):
#     dp[0][col] = dp[0][col - 1] + matrix[0][col]
#
# # Fill rest of the cells
# for row in range(1, rows):
#     for col in range(1, cols):
#         up = dp[row - 1][col]
#         left = dp[row][col - 1]
#         dp[row][col] = max(up, left) + matrix[row][col]
#
# path = deque()
# row = len(dp) - 1
# col = len(dp[0]) - 1
#
# while row > 0 and col > 0:
#     path.appendleft([row, col])
#     if dp[row - 1][col] > dp[row][col - 1]:
#         row -= 1
#     else:
#         col -= 1
# for idx in range(row, 0, -1):
#     path.appendleft([idx, col])
# for idx in range(col, 0, -1):
#     path.appendleft([row, idx])
# path.appendleft([0, 0])
#
# print(*path)
#

# Solution 2 - THE SAME!
from collections import deque

rows = int(input())
cols = int(input())

matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]
for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

# for row in dp:
#     print(row)

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

# for row in dp:
#     print(row)

path = deque()
row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    path.appendleft([row, col])
    if dp[row][col - 1] >= dp[row - 1][col]:
        col -= 1
    else:
        row -= 1

while row > 0:
    path.appendleft([row, col])
    row -= 1
while col > 0:
    path.appendleft([row, col])
    col -= 1

path.appendleft([0, 0])

print(*path)
