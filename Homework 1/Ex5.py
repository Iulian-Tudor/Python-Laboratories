def print_spiral(matrix):
    final = []

    if len(matrix) == 0:
        return final

    top = 0
    left = 0
    bottom = len(matrix)-1
    right = len(matrix[0])-1

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            final.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            final.append(matrix[i][right])
        right -= 1

        if top <= bottom and left <= right:
            for i in range(right, left - 1, -1):
                final.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                final.append(matrix[i][left])
            left += 1

    return final


def main():
    matrice = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']]

    for x in print_spiral(matrice):
        print(x, end=" ")
    print()


main()
