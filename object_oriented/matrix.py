"""
This is a self-defined project in order to practice Linear Algebra.
It is me trying to do matrix calculations without using numpy package.

The project is not finished.

Future goals:
- gaussian elmination
- determinant
- inverse of a matrix
"""


"""
09 August, 2020
10 Agust, 2020
Third file
"""


class Matrix:
    def __init__(self, mat, vertical=False):
        self.mat = mat
        self.vertical = vertical

    @property
    def mat(self):
        return self.__mat

    @mat.setter
    def mat(self, mat):
        if not (isinstance(mat, list) or isinstance(mat, tuple)):
            self.__mat = [[mat]]
        elif not isinstance(mat[0], list):
            if self.__vertical:
                result = []
                for each in mat:
                    result.append([each])
                self.__mat = result
            else:
                self.__mat = [mat]
        else:
            self.__mat = mat

    # @property
    # def vertical(self):
    #     return self.__vertical
    #
    # @vertical.setter
    # def vertical(self, vertical):
    #     self.__vertical = vertical

    def __len__(self):
        return int(str(self.size()[0]) + str(self.size()[1]))

    def size(self):
        return len(self.__mat), len(self.__mat[0])

    def issame_dimensions(self, other):
        return self.size() == other.size()

    def __add__(self, other):
        if not self.issame_dimensions(other):
            raise ValueError("Dimensions must agree")
        addition = [[0 for each in range(len(every))] for every in self.__mat]
        for each in range(len(addition)):
            for every in range(len(addition[0])):
                addition[each][every] = self.__mat[each][every] + \
                                        other.__mat[each][every]
        return Matrix(addition)

    def __sub__(self, other):
        if not self.issame_dimensions(other):
            raise ValueError("Dimensions must agree")

        subtraction = [[0 for each in range(len(every))] for every in self.__mat]
        for each in range(len(subtraction)):
            for every in range(len(subtraction[0])):
                subtraction[each][every] = self.__mat[each][every] - \
                                           other.__mat[each][every]
        return Matrix(subtraction)

    def transpose(self):
        t = [[0 for each in self.__mat]
             for every in range(len(self.__mat[0]))]
        for each in range(len(self.__mat[0])):
            for every in range(len(self.__mat)):
                t[each][every] = self.__mat[every][each]
        return Matrix(t)

    def __mul__(self, other):
        """Currently, just computes integer to matrix scalar multiplication
           just works in this structure: matrix * int
                10 August
        """
        result = [[0 for each in range(len(every))] for every in self.__mat]
        if isinstance(other, int):
            for each in range(len(self.__mat)):
                for every in range(len(self.__mat[0])):
                    result[each][every] = other * self.__mat[each][every]
        return Matrix(result)

    def __eq__(self, other):
        return self.__mat == other.__mat

    def __ne__(self, other):
        return not self.__eq__(other)

    def issymmetric(self):
        return self == self.transpose()

    def __str__(self):
        return "MATRIX\t" + "\n\t\t".join(" ".join(str(every) for every in each)
                                          for each in self.__mat)


if __name__ == '__main__':
    matrix_01 = Matrix([[1, 2], [3, 4]])
    print(matrix_01)
    matrix_04 = Matrix(5)
    print(matrix_04)
    matrix_02 = Matrix([[1], [1]])
    print(matrix_02.issymmetric())
    # print(matrix_01 + matrix_02)  # exception
    print(matrix_02.size())
    print(matrix_01.size())
    print(matrix_01.issame_dimensions(matrix_02))
    print(matrix_02)