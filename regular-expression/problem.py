def operator_star_definition(str):
    return len(str) >= 0


def operator_ques_definition(str):
    return len(str) == 1


def operate(operator, operator_alphabets):
    if operator == "*":
        return operator_star_definition(operator_alphabets)
    if operator == "?":
        return operator_ques_definition(operator_alphabets)


def get_alphabet_of_operators(str, operator_alphabets_markers):
    """
    # abcd => 0101 => ["a", "c"]
    :param str:
    :param operator_alphabets_markers:
    :return:
    """
    str_arr = list(str)
    for i, operator_alphabets_marker in enumerate(operator_alphabets_markers):
        if operator_alphabets_marker == 1:
            str_arr[i] = " "
    return "".join(str_arr).split(" ")


def are_alphabets_present_in_same_sequence_in_str_and_pattern_and_return_operator_alphabets(str, alphabets):
    if len(alphabets) == 0:
        return False, [str]
    pos = 0
    operator_alphabets_markers = [0] * len(str)
    for index, char in enumerate(str):
        if char == alphabets[pos]:
            pos += 1
            operator_alphabets_markers[index] = 1
    # abcd => 0101 => ["a", "c"]
    alphabet_operator = get_alphabet_of_operators(str, operator_alphabets_markers)
    return pos == len(alphabets), alphabet_operator


def regular_expression(str, pattern):
    operator_star, has_star = "*", False
    operator_ques, has_ques = "?", False

    operators = []
    alphabets = []
    for char in pattern:
        if char == operator_ques or char == operator_star:
            operators.append(char)
        else:
            alphabets.append(char)

    if len(operators) == 0:
        return str == pattern

    else:
        if len(alphabets) == 0:

            if alphabets.__contains__(operator_star):
                return True
            else:
                if alphabets.__contains__(operator_ques):
                    return len(str) == len(pattern)
        else:
            return compare_alphabets_and_operators(alphabets, operators, str)


def compare_alphabets_and_operators(alphabets, operators, str):
    _are_alphabets_present_in_same_sequence_in_str_and_pattern, operator_alphabets = \
        are_alphabets_present_in_same_sequence_in_str_and_pattern_and_return_operator_alphabets(str, alphabets)
    operator_results = []
    if _are_alphabets_present_in_same_sequence_in_str_and_pattern:
        for i, operator in enumerate(operators):
            if operator_alphabets[i] == "":
                continue
            operator_result = operate(operators, operator_alphabets[i])
            operator_results.append(operator_result)
    results = list(filter(lambda e: e == False, operator_results))
    return len(results) == 0


def test():
    print(regular_expression("aa", "a") == False)
    print(regular_expression("aa", "*") == True)
    print(regular_expression("aa", "*?") == True)
    print(regular_expression("cb", "*a") == False)
    print(regular_expression("adceb", "*a*b") == True)  # ["dce", "e"] == [*, *]
    print(regular_expression("acdcb", "a*c?b") == False)


test()
