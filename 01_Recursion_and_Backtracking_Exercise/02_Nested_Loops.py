# # solution 1
# def nested_loops(idx, vect, symbols):
#     if idx >= len(vect):
#         print(*vect, sep=' ')
#         return
#
#     for num in symbols:
#         vect[idx] = num
#         nested_loops(idx + 1, vect, symbols)
#
#
# n = int(input())
# vector = [0] * n
# elements = []
# for i in range(n):
#     elements.append(i + 1)
#
# nested_loops(0, vector, elements)

# solution 2
def nested_loops(idx, array):
    if idx >= len(array):
        print(*array, sep=' ')
        return
    for num in range(1, len(array) + 1):
        array[idx] = num
        nested_loops(idx + 1, array)


n = int(input())
arr = [None] * n

nested_loops(0, arr)
