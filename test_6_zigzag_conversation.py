"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""
import pytest


def convert(input, rows_num):
    if rows_num == 1 or len(input) <= 1:
        return input
    result = []
    step = (rows_num - 1) * 2
    for line_num in range(rows_num):
        for i in range(0, len(input) - line_num, step):
            result.append(i + line_num)
            right_candidate = i + step - line_num
            if line_num != 0 and line_num != (rows_num - 1) and right_candidate < len(input):
                result.append(right_candidate)
    return "".join([input[i] for i in result])


def convert_alternative(input, rows_num):
    if rows_num == 1 or len(input) <= 1:
        return input

    result = [""] * rows_num
    current_row = 0
    going_down = False

    for char in input:
        result[current_row] += char
        if current_row == 0 or current_row == rows_num - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return "".join(result)


@pytest.mark.parametrize("input, rows_num, expected", [("A", 1, "A"),
                                                       ("AA", 1, "AA"),
                                                       ("", 1, ""),
                                                       ("", 10, ""),
                                                       ("ABCDEFGHI", 1, "ABCDEFGHI"),
                                                       ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
                                                       ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
                                                       ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
                                                       ("AA", 2, "AA")])
def test_main_func(input, rows_num, expected):
    assert convert(input, rows_num) == expected


@pytest.mark.parametrize("input, rows_num, expected", [("A", 1, "A"),
                                                       ("AA", 1, "AA"),
                                                       ("", 1, ""),
                                                       ("", 10, ""),
                                                       ("ABCDEFGHI", 1, "ABCDEFGHI"),
                                                       ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
                                                       ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
                                                       ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
                                                       ("AA", 2, "AA")])
def test_alt_func(input, rows_num, expected):
    assert convert_alternative(input, rows_num) == expected

