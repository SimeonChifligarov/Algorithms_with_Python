from collections import deque

words = input().split()

length = len(words)
size = [0] * length
prev = [0] * length

best_size = 0
best_idx = 0

for idx in range(length):
    current_word = words[idx]
    current_size = 1
    parent = None

    for prev_idx in range(idx - 1, -1, -1):
        prev_word = words[prev_idx]

        if len(prev_word) >= len(current_word):
            continue

        new_size = size[prev_idx] + 1
        if new_size >= current_size:
            current_size = new_size
            parent = prev_idx

    size[idx] = current_size
    prev[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

# print(best_size)
# print(best_idx)

lis = deque()  # longest increasing subsequence

idx = best_idx
while idx is not None:
    lis.appendleft(words[idx])
    idx = prev[idx]

print(*lis)
