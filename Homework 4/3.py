class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 < row < self.rows or 0 < col < self.cols:
            return self.data[row][col]

    def set(self, row, col, value):
        if 0 < row < self.rows or 0 < col < self.cols:
            self.data[row][col] = value
            return True

    def transpose(self):
        return [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]

    def multiply(self, other):
        if self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result

    def transform(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])


def fill_matrix(matrix):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            matrix.set(i, j, i+j)


def get_matrix(matrix):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            print(matrix.get(i, j), end=' ')
        print()


def main():
    matrix = Matrix(7, 7)
    fill_matrix(matrix)

    get_matrix(matrix)

    print(matrix.transpose())

    matrix.transform(lambda x: x * 2)


main()
