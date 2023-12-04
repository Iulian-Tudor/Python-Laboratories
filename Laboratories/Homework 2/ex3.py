def multimi(x, y):
    intersectie = list(set(x).intersection(y))
    reuniune = list(set(x).union(y))
    x_fara_y = list(set(x).difference(y))
    y_fara_x = list(set(y).difference(x))

    return intersectie, reuniune, x_fara_y, y_fara_x


def main():
    x = [6, 7, 8, 9, 10]
    y = [3, 4, 5, 6, 7]
    final = multimi(x, y)
    print("Intersectie: ", final[0])
    print("Reuniune: ", final[1])
    print("X fara Y: ", final[2])
    print("Y fara X: ", final[3])


main()
