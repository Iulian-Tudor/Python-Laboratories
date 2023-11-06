class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        return self.data[row][col]

    def set(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        self.data[row][col] = value
        return True

    def transpose(self):
        return [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]

    def multiply(self, other):
        if self.cols != other.rows:
            return None
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


def main():
    matrix = Matrix(3, 3)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)
    matrix.set(2, 0, 7)
    matrix.set(2, 1, 8)
    matrix.set(2, 2, 9)
    print(matrix.get(0, 0))
    print(matrix.get(1, 1))
    print(matrix.transpose())
    print(matrix.multiply(matrix).get(0, 0))
    matrix.transform(lambda x: x * 2)
    print(matrix.get(0, 0))


main()
