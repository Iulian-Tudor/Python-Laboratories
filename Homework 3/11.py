def subset(*args, **kwargs):
    keyword_values = set(kwargs.values())
    count = 0

    for arg in args:
        if arg in keyword_values:
            count += 1

    return count


def main():
    print(subset(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3, d=4, e=5, f=6, g=7))


main()