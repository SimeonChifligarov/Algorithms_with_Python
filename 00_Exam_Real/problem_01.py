def find_conditional_operator_result(statement):
    list_of_quest = [1 for e in statement.split() if e == '?']
    if len(list_of_quest) == 1:
        tokens = statement.split()
        boolean = tokens[0]
        position = 0
        for i in range(len(statement) - 1, -1, -1):
            if statement[i] == ':':
                position = i
                break
        if boolean == 't':
            return ''.join(statement[4:i - 1])
        return ''.join(statement[i + 2:])

    current_tokens = statement.split()
    position = 0
    for i in range(len(statement) - 1, -1, -1):
        if statement[i] == ':':
            position = i
            break
    current_statement = ''.join(statement[4:i - 1])
    # current_result = find_conditional_operator_result(current_statement)
    # new_statement = ' '.join(current_tokens[:position - 3]) + ' ' + current_result + ' ' + ' '.join(
    #     current_tokens[position + 2:])

    return find_conditional_operator_result(current_statement)


conditional_operator_input = input()
result = find_conditional_operator_result(conditional_operator_input)

print(result)
