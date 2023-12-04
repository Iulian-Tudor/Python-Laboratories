def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fibonacci(n - 2) + fibonacci(n - 1)


def main():
    n = int(input("Enter a number: "))
    for i in range(0, n):
        print(fibonacci(i), end=" ")


main()
