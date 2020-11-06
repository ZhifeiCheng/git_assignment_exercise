"""
Name: Zhifei Cheng
UWNetId: zc5dp
TimeComplexity = O(n)
"""


def is_palindrome(the_string: str) -> bool:
    """
    Evaluates a given string and determines whether or not it is a palindrome.
    :param the_string: The string to evaluate.
    :returns: True when the string is a palindrome, False otherwise.
    """
    s = the_string.lower()
    # left pointer
    i = 0
    # right pointer
    j = len(s)-1
    # before the left pointer and right pointer meets
    while i < j:
        # if meet white space, the left pointer will move forward without doing anything.
        while i < j and s[i] == " ":
            i += 1
        # if meet white space, the right pointer will move forward without doing anything.
        while i < j and s[j] == " ":
            j -= 1
        # test if the char at left pointer equals with char at the right pointer , if yes,
        # left and right pointer move forward to test next pair of chars
        if s[i] == s[j]:
            i += 1
            j -= 1
        # if not, the string is not a palindrome, return False
        else:
            return False
    else:
        return True
