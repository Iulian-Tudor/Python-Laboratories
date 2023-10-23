def compare(x, y):
    if type(x) != type(y):
        return False
    if isinstance(x, dict):
        if len(x) != len(y):
            return False
        for key in x:
            if key not in y:
                return False
            if not compare(x[key], y[key]):
                return False
        return True
    elif isinstance(x, (list, tuple, set)):
        if len(x) != len(y):
            return False
        for i in range(len(x)):
            if not compare(x[i], y[i]):
                return False
        return True
    else:
        return x == y


def main():
    x = {1: 2, 3: 4, 5: 6}
    y = {1: 2, 3: 4, 5: 6}
    print(compare(x, y))

    a = {1: 2, 3: 4, 5: 6}
    b = {1: [2, 3], 3: 4, 5: 6}
    print(compare(a, b))


if __name__ == '__main__':
    main()