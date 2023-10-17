def order_tuple(tupla):

    def custom_key(cheie):
        if len(cheie[1]) >= 3:
            return cheie[1][2]
        else:
            return ''

    return sorted(tupla, key=custom_key)


def main():
    lst = [('abc', 'bcd'), ('abc', 'zza')]
    print(order_tuple(lst))


main()
