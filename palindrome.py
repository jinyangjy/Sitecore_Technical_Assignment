def is_palindrome(input_string, trash_symbols_string):
    """
    Approach Description:
    The approach used in this function is a two pointer technique, while filtering the trash symbols to check if the string
    is a palindrome. It starts of by initialising the two pointers, left and right,one at the start of the string (Index 0)
    and the other at the end of the string(Last character of the string). It continues to iterate as long as the left pointer
    is less than the right pointer. In each iteration, two characters are "left_char" and "right_char", both of which are
    converted to lowercase. In order to filter the trash symbols, there are two inner loops which is used to increment the
    left and right pointers until the characters are not trash symbols. If the left and right characters at the current
    position are equal, it will increment for the left and decrement for the right to move them closer for the next iteration.
    The loop continues to run until either a mismatched has been found which returns False, or the "left" pointer is >= "right"
    pointer which returns True.

    Parameters:
    input_string (string): The string to be checked.
    trash_symbols_string (string): The string of trash symbols to be filtered.

    Returns:
    True (boolean): If the string is a palindrome.
    False (boolean): If the string is not a palindrome.

    Time Complexity: O(n), where n is the length of the input string.

    Aux Space Complexity: O(1), operations are directly perfomed on the given strings.
    """
    left = 0
    right = len(input_string) - 1

    while left < right:
        left_char = input_string[left].lower()
        right_char = input_string[right].lower()

        while left < right and (left_char in trash_symbols_string.lower()):
            left += 1
            left_char = input_string[left].lower()

        while left < right and (right_char in trash_symbols_string.lower()):
            right -= 1
            right_char = input_string[right].lower()

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True
