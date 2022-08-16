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
        for i in range(0, len(input) - 1, step):
            left_candidate = i + line_num
            if left_candidate < len(input) and left_candidate not in result:
                result.append(left_candidate)
            right_candidate = i + step - line_num
            if right_candidate < len(input) and right_candidate not in result:
                result.append(right_candidate)
    return "".join([input[i] for i in result])


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