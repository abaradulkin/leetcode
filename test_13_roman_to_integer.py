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

    def roman_to_int(self, s: str) -> int:
        result = 0
        for symbol in self.symbols.keys():
            while s:
                if s.startswith(symbol):
                    result += self.symbols[symbol]
                    s = s.removeprefix(symbol)
                else: break
        return result


class SolutionOptimized:
    symbols = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    def roman_to_int(self, s: str) -> int:
        result, previous = 0, 0
        for i in range(len(s) - 1):
            candidate = self.symbols[s[i]]
            next = self.symbols[s[i + 1]]
            if candidate < next:
                result -= candidate
            else:
                result += candidate
        result += self.symbols[s[-1]]
        return result


@pytest.mark.parametrize("input,output", (("III", 3),
                                          ("LVIII", 58),
                                          ("MCMXCIV", 1994)))
def test_main_function(input, output):
    sol = Solution()
    assert sol.roman_to_int(input) == output


@pytest.mark.parametrize("input,output", (("III", 3),
                                          ("LVIII", 58),
                                          ("MCMXCIV", 1994)))
def test_optimized_function(input, output):
    sol = SolutionOptimized()
    assert sol.roman_to_int(input) == output
