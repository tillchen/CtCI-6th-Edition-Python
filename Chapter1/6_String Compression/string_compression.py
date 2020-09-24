from itertools import groupby
import unittest


def string_compression(s: str) -> str:
    s_compressed = ''
    for char, repetition in groupby(s):
        s_compressed += f'{char}{repetition}'
    if len(s_compressed) >= len(s):
        return s
    return s_compressed


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
