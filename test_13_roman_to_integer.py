import pytest


# https://leetcode.com/problems/roman-to-integer/
class Solution:
    symbols = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        for symbol in self.symbols.keys():
            while s:
                if s.startswith(symbol):
                    result += self.symbols[symbol]
                    s = s.removeprefix(symbol)
                else: break
        return result


@pytest.mark.parametrize("input,output", (("III", 3),
                                          ("LVIII", 58),
                                          ("MCMXCIV", 1994)))
def test_main_function(input, output):
    sol = Solution()
    assert sol.romanToInt(input) == output
