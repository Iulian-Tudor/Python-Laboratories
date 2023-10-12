def count_bit(number):
    print(number.bit_count())


def main():
    sample = input("Enter a number: ")
    count_bit(int(sample))


main()
