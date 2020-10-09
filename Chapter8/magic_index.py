from typing import List


def magic_index(L: List[int]) -> int:
    """
    Returns the magic index if it exists. O(n) time and O(1) space.

    L is already sorted.
    """

    for i, item in enumerate(L):
        if item == i:
            return i

    return -1


def magic_index_binary_search(L: List[int]) -> int:
    """
    Ditto. O(log n) time and O(1) space.
    """

    left, right = 0, len(L) - 1
    while left <= right:
        middle = (left + right) // 2
        if L[middle] == middle:
            return middle
        elif L[middle] < middle:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == '__main__':
    print(magic_index([-3, -2, 0, 3, 5]))
    print(magic_index_binary_search([-3, -2, 0, 3, 5]))
