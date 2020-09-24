import unittest


def string_rotation(s1: str, s2: str) -> bool:
    """s1=xy, s2=yx, s2s2=yxyx"""
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
