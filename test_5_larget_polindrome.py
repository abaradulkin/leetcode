def is_polindrome(s):
    if s == s[::-1]:
        return True


def longest_palindrome(s: str) -> str:
    """ Given a string s, return the longest palindromic substring in s. """
    total = len(s)
    if total < 2:
        return s
    largest = s[0]
    for l in range(total):
        for r in range(total - 1, l + len(largest) - 1, -1):
            if s[l] == s[r] and is_polindrome(s[l: r + 1]):
                largest = max(largest, s[l: r + 1], key=len)
        if total - l - 1 < len(largest):
            break
        l += 1
    return largest
