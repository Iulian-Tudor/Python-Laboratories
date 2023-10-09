

# Ex1

def ex1(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def main():
    print(ex1(20, 10))


main()
