def group_rhyme(words):
    rhymes = {}
    for word in words:
        rima = word[-2:]

        if rima in rhymes:
            rhymes[rima].append(word)
        else:
            rhymes[rima] = [word]

    sorted_rhymes = list(rhymes.items())

    return sorted_rhymes


def main():
    words = ["ana", "banana", "mere", "arme", "pere"]
    print(group_rhyme(words))


main()
