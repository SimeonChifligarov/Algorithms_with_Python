def count_all_paths(r, c, rows, cols):
    if r >= rows or c >= cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1

    result = 0
    result += count_all_paths(r, c + 1, rows, cols)  # Right
    result += count_all_paths(r + 1, c, rows, cols)  # Down

    return result


current_rows = int(input())
current_cols = int(input())

print(count_all_paths(0, 0, current_rows, current_cols))
