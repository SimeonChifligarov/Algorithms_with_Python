# # solution 1
# def generate_0_1(idx, vect):
#     if idx >= len(vect):
#         print(*vect, sep=' ')
#         return
#
#     for num in range(2):
#         vect[idx] = num
#         generate_0_1(idx + 1, vect)

# solution 2
def generate_0_1(idx, vect):
    if idx >= len(vect):
        print(*vect, sep='')
        return

    symbol_1 = 0
    symbol_2 = 1
    symbols = [symbol_1, symbol_2]

    for num in symbols:
        vect[idx] = num
        generate_0_1(idx + 1, vect)


n = int(input())
vector = [0] * n

generate_0_1(0, vector)
