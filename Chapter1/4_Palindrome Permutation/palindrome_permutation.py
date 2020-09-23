from collections import Counter
import unittest


def palindrome_permutation(string: str) -> bool:
    string_without_spaces = string.replace(' ', '').lower()
    is_odd = len(string_without_spaces) % 2
    odd_occurred = False
    counter = Counter(string_without_spaces)
    for value in counter.values():
        if value % 2 == 1:
            if not is_odd or odd_occurred:
                return False
            odd_occurred = True
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
