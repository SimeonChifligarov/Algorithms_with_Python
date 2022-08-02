# Write a program that reverses and prints an array. Use recursion.
#
# # just testing Judge (points gained without recursion)
# input_list = [int(el) for el in input().split()]
# print(' '.join([str(el) for el in input_list[::-1]]))

# # just testing
# elements = input().split()
# for left_idx in range(len(elements) // 2):
#     right_idx = len(elements) - 1 - left_idx
#     elements[left_idx], elements[right_idx] = elements[right_idx], elements[left_idx]
# print(' '.join(elements))

# solution
def reverse_array(left_idx, array):
    if left_idx >= len(array) // 2:
        return
    right_idx = len(array) - 1 - left_idx
    array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
    reverse_array(left_idx + 1, array)


elements = input().split()

reverse_array(0, elements)
print(*elements)
