import pytest


def length_of_unique_substring(s: str) -> int:
    """ Given a string s, find the length of the longest substring without repeating characters. """
    result = set()

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
                                          ("b", 1),
                                          ("pwwkew", 3)))
def test_main_function(input, output):
    assert length_of_unique_substring(input) == output
