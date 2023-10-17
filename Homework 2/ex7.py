def is_palindrome(s):
    return s == s[::-1]


def greatest_palindrom_in_list(lst):
    palindroms = []
    n = 0
    for item in lst:
        if is_palindrome(item):
            n += 1
            palindroms.append(item)
    return n, max(palindroms)


def main():
    x = int(input("Introduceti numarul de elemente din lista: "))
    lst = []
    for i in range(0, x):
        element = input()
        lst.append(element)
    print(greatest_palindrom_in_list(lst))


main()
