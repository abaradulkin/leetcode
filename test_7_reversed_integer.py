import pytest


def reverse(x: int) -> int:
    if x >= 2 ** 31 - 1 or x <= -2 ** 31:
        return 0
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)
    string_repr = str(x)
    string_repr = string_repr[::-1]
    result = int(string_repr) * sign
    if result >= 2 ** 31 - 1 or result <= -2 ** 31:
        return 0
    return result


@pytest.mark.parametrize("x, y", [(0, 0),
                                  (123, 321),
                                  (-321, -123),
                                  (100, 1),
                                  (-9000, -9),
                                  (2 ** 31 - 2, 0),
                                  (2 ** 31 - 1, 0),
                                  (-2 ** 31 - 1, 0),
                                  (-2 ** 31, 0),
                                  (2147483111, 1113847412),
                                  (-2147481321, -1231847412),
                                  (1073741828, 0),
                                  (-1073741828, 0)])
def test(x, y):
    assert reverse(x) == y
