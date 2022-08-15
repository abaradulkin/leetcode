import pytest
from itertools import combinations


def length_of_unique_substring_optimal(s: str) -> int:
    duplicates = {}
    result = 0
    start = 0

    for end in range(len(s)):
        duplicate_index = duplicates.get(s[end], None)
        if duplicate_index is not None:
            result = max(result, end - start)
            for i in range(start, duplicate_index):
                del(duplicates[s[i]])
            start = duplicate_index + 1
        duplicates[s[end]] = end
    result = max(result, len(s) - start)
    return result


def length_of_unique_substring_via_itertools(test_str: str) -> int:
    res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r=2)]
    res = [x for x in res if len(x) == len(set(x))]
    if res:
        return len(max(res, key=len))
    return 0


def length_of_unique_substring(s: str) -> int:
    """ Given a string s, find the length of the longest substring without repeating characters. """
    result = 0

    for i in range(len(s)):
        last_lenght = 0
        candidate = set()
        for char in s[i:]:
            candidate.add(char)
            if len(candidate) > last_lenght:
                last_lenght += 1
                if len(candidate) > len(result):
                    result = candidate
            else:
                break
        else:
            return len(result)


@pytest.mark.parametrize("input,output", (("abcabcabc", 3),
                                          ("bbbbb", 1),
                                          ("dvdf", 3),
                                          ("b", 1),
                                          ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}", 93),
                                          ("", 0),
                                          ("pwwkew", 3)))
def test_main_function_optimal(input, output):
    assert length_of_unique_substring_optimal(input) == output


@pytest.mark.parametrize("input,output", (("abcabcabc", 3),
                                          ("bbbbb", 1),
                                          ("dvdf", 3),
                                          ("b", 1),
                                          ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}", 93),
                                          ("", 0),
                                          ("pwwkew", 3)))
def test_main_function(input, output):
    assert length_of_unique_substring(input) == output


@pytest.mark.parametrize("input,output", (("abcabcabc", 3),
                                          ("bbbbb", 1),
                                          ("dvdf", 3),
                                          ("b", 1),
                                          ("", 0),
                                          ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}", 93),
                                          ("pwwkew", 3)))
def test_main_function_via_itertools(input, output):
    assert length_of_unique_substring_via_itertools(input) == output

