cables = [int(el) for el in input().split()]
size = len(cables) + 1

positions = [pos for pos in range(1, size)]

# print(cables)
# print(positions)

lcs = [[0] * size for _ in range(size)]  # longest common subsequence

# for row in lcs:
#     print(row)

for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == positions[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])

result = lcs[size - 1][size - 1]
print(f'Maximum pairs connected: {result}')
