def cannot_see(matrice):
    lst = []
    n=0
    for i in range(1, len(matrice)):
        for j in range(len(matrice[0])):
            for k in range (1,i):
                if matrice[i][j] < matrice[i-k][j]:
                    lst.append((i, j))
    return lst


def main():
    field = [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 7, 2],
             [5, 5, 2, 5, 6, 4],
             [6, 6, 7, 6, 7, 5]]

    print(cannot_see(field))


main()
