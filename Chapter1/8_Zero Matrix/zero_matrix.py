from typing import List
import unittest


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rows, columns = set(), set()
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 0:
                rows.add(i)
                columns.add(j)
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if i in rows or j in columns:
                matrix[i][j] = 0
    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
