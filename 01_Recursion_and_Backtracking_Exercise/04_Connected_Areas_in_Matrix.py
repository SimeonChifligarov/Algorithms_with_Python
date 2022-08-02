class Area:
    def __init__(self, r, c, sz):
        self.row = r
        self.col = c
        self.size = sz


def explore_area(r, c, mtrx):
    if r < 0 or c < 0 or r >= len(mtrx) or c >= len(mtrx[0]):
        return 0
    if not mtrx[r][c] == '-':
        return 0

    mtrx[r][c] = 'v'  # visited

    result = 1
    result += explore_area(r - 1, c, mtrx)  # Up
    result += explore_area(r + 1, c, mtrx)  # Down
    result += explore_area(r, c - 1, mtrx)  # Left
    result += explore_area(r, c + 1, mtrx)  # Right

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []

for row in range(rows):
    for col in range(cols):
        if not matrix[row][col] == '-':
            continue
        size = explore_area(row, col, matrix)
        # if size == 0:
        #     continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
