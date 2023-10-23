def return_touple(list):
    unique = len(set(list))
    repeating = len(list) - unique
    return (unique, repeating)


def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(return_touple(list))


main()