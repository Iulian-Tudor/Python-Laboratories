def ascii_character(lists, x=1, flag=True):
    final = []

    for word in lists:
        filtru = []
        for char in word:
            ascii_code = ord(char)
            if (ascii_code % x == 0 and flag) or (not flag and ascii_code % x != 0):
                filtru.append(char)
        final.append(filtru)

    return final


def main():
    x = 2
    lst = ["ana", "are", "mere", "si", "pere"]
    flag = False

    print(ascii_character(lst, x, flag))


main()
