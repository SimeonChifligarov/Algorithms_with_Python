# Backtracking Algorithm (Pseudocode)
#
# static void recurrence(Node node) {
#   if (node is solution) {
#     printSolution(node);
#   } else {
#     for each child c of node
#       if (c is perspective candidate) {
#      markPositionVisited(c);
#      recurrence(c);
#      unmarkPositionVisited(c);
#   }
# }

# # solution 1
# def find_all_paths(row, col, lab, direction, path):
#     if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
#         return
#     if lab[row][col] == 'e':
#         path.append(direction)
#         print(''.join(path))
#         path.pop()
#         return
#     if lab[row][col] == '*':
#         return
#     if lab[row][col] == 'v':
#         return
#
#     lab[row][col] = 'v'
#     path.append(direction)
#
#     find_all_paths(row - 1, col, lab, 'U', path)
#     find_all_paths(row + 1, col, lab, 'D', path)
#     find_all_paths(row, col - 1, lab, 'L', path)
#     find_all_paths(row, col + 1, lab, 'R', path)
#     lab[row][col] = '-'
#
#     path.pop()

# # solution 2
# def find_all_paths(row, col, lab, direction, path):
#     if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
#         return
#     if lab[row][col] == '*':
#         return
#     if lab[row][col] == 'v':
#         return
#
#     path.append(direction)
#     if lab[row][col] == 'e':
#         print(''.join(path))
#     else:
#         lab[row][col] = 'v'
#
#         find_all_paths(row - 1, col, lab, 'U', path)
#         find_all_paths(row + 1, col, lab, 'D', path)
#         find_all_paths(row, col - 1, lab, 'L', path)
#         find_all_paths(row, col + 1, lab, 'R', path)
#         lab[row][col] = '-'
#
#     path.pop()

# solution 3
def is_position_invalid(r, c, mtrx):
    if r < 0 or c < 0 or r >= len(mtrx) or c >= len(mtrx[0]):
        return True


def is_cell_visited(r, c, mtrx, sym):
    if mtrx[r][c] == sym:
        return True


def is_cell_wall(r, c, mtrx, sym):
    if mtrx[r][c] == sym:
        return True


def is_cell_exit(r, c, mtrx, sym):
    if mtrx[r][c] == sym:
        return True


def find_all_paths(row, col, lab, direction, path):
    wall_symbol = '*'
    visited_symbol = 'v'
    exit_symbol = 'e'
    path_symbol = '-'

    # could union next 3 checks in 1 function "is_potential_solution"

    if is_position_invalid(row, col, lab):
        return
    if is_cell_wall(row, col, lab, wall_symbol):
        return
    if is_cell_visited(row, col, lab, visited_symbol):
        return

    path.append(direction)

    if is_cell_exit(row, col, lab, exit_symbol):
        print(''.join(path))
    else:
        lab[row][col] = visited_symbol

        find_all_paths(row - 1, col, lab, 'U', path)
        find_all_paths(row + 1, col, lab, 'D', path)
        find_all_paths(row, col - 1, lab, 'L', path)
        find_all_paths(row, col + 1, lab, 'R', path)
        lab[row][col] = path_symbol

    path.pop()


rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

# print(matrix)

find_all_paths(0, 0, matrix, '', [])
