def replace_diagonal(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i+1][j] = 0
    return matrix


def main():
    matrice = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    result = replace_diagonal(matrice)
    for line in result:
        print(line)


main()
