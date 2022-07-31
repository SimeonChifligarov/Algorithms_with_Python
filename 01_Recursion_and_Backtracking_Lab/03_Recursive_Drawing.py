def draw_figure(count_symbols):
    upper_symbol = '*'
    lower_symbol = '#'

    if count_symbols == 0:
        return

    print(upper_symbol * count_symbols)  # pre-action(s)
    draw_figure(count_symbols - 1)
    print(lower_symbol * count_symbols)  # post-action(s)


n = int(input())

draw_figure(n)
