from collections import Counter
import unittest


def check_permutation(string_1: str, string_2: str) -> bool:
    # O(nlogn) time and O(1) space.
    return sorted(string_1) == sorted(string_2)


def check_permutation_linear_time(string_1: str, string_2: str) -> bool:
    # O(n) time and O(n) space.
    return Counter(string_1) == Counter(string_2)


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
            result = check_permutation_linear_time(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)
            result = check_permutation_linear_time(*test_strings)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
