import itertools
from math import sqrt


class matrix:

    # implements basic operations of a matrix class

    # ------------
    #
    # initialization - can be called with an initial matrix
    #

    def __init__(self, value=None) -> None:
        if value is None:
            value = [[]]
        self.value = value
        self.dimx = len(value)
        self.dimy = len(value[0])
        if value == [[]]:
            self.dimx = 0

    # ------------
    #
    # makes matrix of a certain size and sets each element to zero
    #

    def zero(self, dimx: int, dimy: int) -> "matrix":
        if dimy == 0:
            dimy = dimx
        # check if valid dimensions
        if dimx < 1 or dimy < 1:
            raise ValueError("Invalid size of matrix")
        self.dimx = dimx
        self.dimy = dimy
        self.value = [[0.0 for _ in range(dimy)] for _ in range(dimx)]

    # ------------
    #
    # makes matrix of a certain (square) size and turns matrix into identity matrix
    #

    def identity(self, dim: int) -> "matrix":
        # check if valid dimension
        if dim < 1:
            raise ValueError("Invalid size of matrix")
        self.dimx = dim
        self.dimy = dim
        self.value = [[0.0 for _ in range(dim)] for _ in range(dim)]
        for i in range(dim):
            self.value[i][i] = 1.0
    # ------------
    #
    # prints out values of matrix
    #

    def show(self, txt: str = '') -> None:
        for i in range(len(self.value)):
            print(f'{txt}[' + ', '.join('%.3f' %
                  x for x in self.value[i]) + ']')
        print(' ')

    # ------------
    #
    # defines elmement-wise matrix addition. Both matrices must be of equal dimensions
    #

    def __add__(self, other: "matrix") -> "matrix":
        # check if correct dimensions
        if self.dimx != other.dimx or self.dimy != other.dimy:
            raise ValueError("Matrices must be of equal dimension to add")
        # add if correct dimensions
        res = matrix()
        res.zero(self.dimx, self.dimy)
        for i, j in itertools.product(range(self.dimx), range(self.dimy)):
            res.value[i][j] = self.value[i][j] + other.value[i][j]
        return res

    # ------------
    #
    # defines elmement-wise matrix subtraction. Both matrices must be of equal dimensions
    #

    def __sub__(self, other: "matrix") -> "matrix":
        # check if correct dimensions
        if self.dimx != other.dimx or self.dimy != other.dimy:
            raise ValueError("Matrices must be of equal dimension to subtract")
        # subtract if correct dimensions
        res = matrix()
        res.zero(self.dimx, self.dimy)
        for i, j in itertools.product(range(self.dimx), range(self.dimy)):
            res.value[i][j] = self.value[i][j] - other.value[i][j]
        return res

    # ------------
    #
    # defines multiplication. Both matrices must be of fitting dimensions
    #

    def __mul__(self, other: "matrix") -> "matrix":
        # check if correct dimensions
        if self.dimy != other.dimx:
            raise ValueError("Matrices must be m*n and n*p to multiply")
        # multiply if correct dimensions
        res = matrix()
        res.zero(self.dimx, other.dimy)
        for i, j in itertools.product(range(self.dimx), range(other.dimy)):
            for k in range(self.dimy):
                res.value[i][j] += self.value[i][k] * other.value[k][j]
        return res

    # ------------
    #
    # returns a matrix transpose
    #

    def transpose(self) -> "matrix":
        # compute transpose
        res = matrix()
        res.zero(self.dimy, self.dimx)
        for i, j in itertools.product(range(self.dimx), range(self.dimy)):
            res.value[j][i] = self.value[i][j]
        return res

    # ------------
    #
    # creates a new matrix from the existing matrix elements.
    #
    # Example:
    #       l = matrix([[ 1,  2,  3,  4,  5],
    #                   [ 6,  7,  8,  9, 10],
    #                   [11, 12, 13, 14, 15]])
    #
    #       l.take([0, 2], [0, 2, 3])
    #
    # results in:
    #
    #       [[1, 3, 4],
    #        [11, 13, 14]]
    #
    #
    # take is used to remove rows and columns from existing matrices
    # list1/list2 define a sequence of rows/columns that shall be taken
    # if no list2 is provided, then list2 is set to list1 (good for
    # symmetric matrices)
    #

    def take(self, list1: list[int], list2: list[int] | None = None) -> "matrix":
        if list2 is None:
            list2 = []
        if list2 == []:
            list2 = list1
        if len(list1) > self.dimx or len(list2) > self.dimy:
            raise ValueError("list invalid in take()")

        res = matrix()
        res.zero(len(list1), len(list2))
        for i, j in itertools.product(range(len(list1)), range(len(list2))):
            res.value[i][j] = self.value[list1[i]][list2[j]]
        return res

    # ------------
    #
    # creates a new matrix from the existing matrix elements.
    #
    # Example:
    #       l = matrix([[1, 2, 3],
    #                  [4, 5, 6]])
    #
    #       l.expand(3, 5, [0, 2], [0, 2, 3])
    #
    # results in:
    #
    #       [[1, 0, 2, 3, 0],
    #        [0, 0, 0, 0, 0],
    #        [4, 0, 5, 6, 0]]
    #
    # expand is used to introduce new rows and columns into an existing matrix
    # list1/list2 are the new indexes of row/columns in which the matrix
    # elements are being mapped. Elements for rows and columns
    # that are not listed in list1/list2
    # will be initialized by 0.0.
    #

    def expand(self, dimx: int, dimy: int, list1: list[int], list2: list[int] | None = None) -> "matrix":
        if list2 is None:
            list2 = []
        if list2 == []:
            list2 = list1
        if len(list1) > self.dimx or len(list2) > self.dimy:
            raise ValueError("list invalid in expand()")

        res = matrix()
        res.zero(dimx, dimy)
        for i, j in itertools.product(range(len(list1)), range(len(list2))):
            res.value[list1[i]][list2[j]] = self.value[i][j]
        return res

    # ------------
    #
    # Computes the upper triangular Cholesky factorization of
    # a positive definite matrix.
    # This code is based on http://adorio-research.org/wordpress/?p=4560
    #

    def Cholesky(self, ztol=1.0e-5) -> "matrix":

        res = matrix()
        res.zero(self.dimx, self.dimx)

        for i in range(self.dimx):
            S = sum((res.value[k][i])**2 for k in range(i))
            d = self.value[i][i] - S
            if abs(d) < ztol:
                res.value[i][i] = 0.0
            elif d < 0.0:
                raise ValueError("Matrix not positive-definite")
            else:
                res.value[i][i] = sqrt(d)
            for j in range(i+1, self.dimx):
                S = sum(res.value[k][i] * res.value[k][j] for k in range(i))
                if abs(S) < ztol:
                    S = 0.0
                try:
                    res.value[i][j] = (self.value[i][j] - S)/res.value[i][i]
                except:
                    raise ValueError("Zero diagonal")
        return res

    # ------------
    #
    # Computes inverse of matrix given its Cholesky upper Triangular
    # decomposition of matrix.
    # This code is based on http://adorio-research.org/wordpress/?p=4560
    #

    def CholeskyInverse(self) -> "matrix":

        res = matrix()
        res.zero(self.dimx, self.dimx)

        # Backward step for inverse.
        for j in reversed(range(self.dimx)):
            tjj = self.value[j][j]
            S = sum(self.value[j][k]*res.value[j][k]
                    for k in range(j+1, self.dimx))
            res.value[j][j] = 1.0 / tjj**2 - S / tjj
            for i in reversed(range(j)):
                res.value[j][i] = res.value[i][j] = (
                    -sum(
                        self.value[i][k] * res.value[k][j]
                        for k in range(i + 1, self.dimx)
                    )
                    / self.value[i][i]
                )
        return res

    # ------------
    #
    # computes and returns the inverse of a square matrix
    #
    def inverse(self) -> "matrix":
        aux = self.Cholesky()
        return aux.CholeskyInverse()

    # ------------
    #
    # prints matrix (needs work!)
    #
    def __repr__(self) -> str:
        return repr(self.value)


def main() -> None:
    omega = matrix([[1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])
    xi = matrix([[5],
                 [0],
                 [0],
                 [0],
                 [0]])

    omega += matrix([[1, -1, 0, 0, 0],
                    [-1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])
    xi += matrix([[-7],
                 [7],
                 [0],
                 [0],
                 [0]])

    omega += matrix([[0, 0, 0, 0, 0],
                    [0, 1, -1, 0, 0],
                    [0, -1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])
    xi += matrix([[0],
                 [-2],
                 [2],
                 [0],
                 [0]])

    omega += matrix([[2, 0, 0, -2, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [-2, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0]])
    xi += matrix([[-4],
                 [0],
                 [0],
                 [4],
                 [0]])

    omega += matrix([[0, 0, 0, 0, 0],
                    [0, 2, 0, 0, -2],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, -2, 0, 0, 2]])
    xi += matrix([[0],
                 [-8],
                 [0],
                 [0],
                 [8]])

    omega += matrix([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 0, -2],
                    [0, 0, 0, 0, 0],
                    [0, 0, -2, 0, 2]])
    xi += matrix([[0],
                 [0],
                 [-4],
                 [0],
                 [4]])

    omega.show("Omega: ")
    xi.show("Xi: ")

    mu = omega.inverse() * xi
    mu.show("Mu: ")


if __name__ == "__main__":
    main()
