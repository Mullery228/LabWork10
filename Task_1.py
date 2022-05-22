from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def __str__(self):
        mat = self.matrix
        a = len(mat[0])
        stroka = str()
        for i in range(0, a + 1):
            if a == len(mat[i]):
                stroka += '\n'
                for j in range(0, len(mat[i])):
                    stroka += str(mat[i][j]) + ' '
            else:
                raise ValueError("fail initialization matrix")
        return stroka

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            Result = self.matrix
        return Matrix(Result)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(second_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """