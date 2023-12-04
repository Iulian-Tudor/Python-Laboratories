def prime_nums(lista):
    lista_prima = []
    for n in lista:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                lista_prima.append(n)
    return lista_prima


def main():
    lst = []
    n = int(input("Enter the number of elements: "))

    for i in range(0, n):
        number = int(input())
        lst.append(number)

    print("Lista initiala: ")
    print(lst)
    print("Lista cu numere prime: ")
    print(prime_nums(lst))


main()
