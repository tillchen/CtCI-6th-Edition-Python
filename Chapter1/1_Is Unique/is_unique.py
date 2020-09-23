from collections import Counter
import unittest


def is_unique(string: str) -> bool:
    # O(n) time and O(n) space.
    if not string:
        return True
    return Counter(string).most_common(n=1)[0][1] == 1


def is_unique_with_constant_space(string: str) -> bool:
    # O(nlogn) time and O(1) space.
    string = ''.join(sorted(string))
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True


def is_unique_with_set(string: str) -> bool:
    # O(n) time and O(n) space.
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True


class Test(unittest.TestCase):
    dataT = ['abcd', 's4fad', '']
    dataF = ['23ds2', 'hb 627jh=j ()']

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
            actual = is_unique_with_constant_space(test_string)
            self.assertTrue(actual)
            actual = is_unique_with_set(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)
            actual = is_unique_with_constant_space(test_string)
            self.assertFalse(actual)
            actual = is_unique_with_set(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
