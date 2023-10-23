from itertools import combinations

def set_operations(*sets):
    set_pairs = list(combinations(sets, 2))
    dictionar = {}

    for x, y in set_pairs:
        k_union = f"{x} | {y}"
        dictionar[k_union] = x.union(y)

        k_intersection = f"{x} & {y}"
        dictionar[k_intersection] = x.intersection(y)

        k_x_minus_y = f"{x} - {y}"
        dictionar[k_x_minus_y] = x.difference(y)

        k_y_minus_x = f"{y} - {x}"
        dictionar[k_y_minus_x] = y.difference(x)

    return dictionar


def main():
    x = {1, 2, 3, 4, 5}
    y = {4, 5, 6, 7, 8}
    z = {7, 8, 9, 10, 11}

    final = set_operations(x, y, z)
    for key, value in final.items():
        print(f"{key} = {value}")


if __name__ == '__main__':
    main()