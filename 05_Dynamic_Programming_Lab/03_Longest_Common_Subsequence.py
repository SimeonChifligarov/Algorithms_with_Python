first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = []

[dp.append([0] * cols) for _ in range(rows)]

# print(dp)

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[rows - 1][cols - 1])

# # taking the individual elements:
# result = []
#
# row = rows - 1
# col = cols - 1
#
# while row > 0 and col > 0:
#     if first[row - 1] == second[col - 1]:
#         result.append(first[row - 1])
#         row -= 1
#         col -= 1
#     elif dp[row - 1][col] > dp[row][col - 1]:
#         row -= 1
#     else:
#         col -= 1
#
# print(result[::-1])

# # # EXTRA NOTES
# # LCS has the following recursive properties:
# lcs[-1][y] = 0
# lcs[x][-1] = 0
# lcs[x][y] = max(
#   lcs[x-1][y],
#   lcs[x][y-1]) or lcs[x-1][y-1]+1 when S1[x] == S2[y]
# # Calculating the LCS Table
# rows = len(first) + 1
# cols = len(second) + 1
# lcs = []
# [lcs.append([0] * cols) for _ in range(rows)]
# for row in range(1, rows):
#     for col in range(1, cols):
#         if first[row - 1] == second[col - 1]:
#             prev = lcs[row - 1][col - 1]
#             lcs[row][col] = prev + 1
#         else:
#             up = lcs[row - 1][col]
#             left = lcs[row][col - 1]
#             lcs[row][col] = max(up, left)
# # Reconstructing the LCS Sequence
# lcs_letters = deque()
# row = rows - 1
# col = cols - 1
# while row >= 0 and col >= 0:
#     if first[row - 1] == second[col - 1]:
#         lcs_letters.appendleft(first[row - 1])
#         row -= 1
#         col -= 1
#     elif lcs[row - 1][col] > lcs[row][col - 1]:
#         row -= 1
#     else:
#         col -= 1
# print(''.join(lcs_letters))
