replacement_cost = int(input())
insert_cost = int(input())
delete_cost = int(input())

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

# dp_2 = [[0] * cols for _ in range(rows)]
# print(dp == dp_2)  # True

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert_cost

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete_cost

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1] + insert_cost,
                               dp[row - 1][col] + delete_cost,
                               dp[row - 1][col - 1] + replacement_cost)

result = dp[rows - 1][cols - 1]
print(f'Minimum edit distance: {result}')
