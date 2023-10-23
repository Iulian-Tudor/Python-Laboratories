def make_dictionary(word):
    dictionary = {}
    for letter in word:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary


def main():
    word = input("Introduceti un cuvant: ")
    print(make_dictionary(word))


main()
