def compose(note, miscari, start):
    song = []
    pivot = start
    song.append(note[start])
    for i in miscari:
        pivot = (pivot + i) % len(note)
        song.append(note[pivot])

    return song


def main():
    note = ["do", "re", "mi", "fa", "sol", "la", "si"]
    miscari = [1, -3, 4, 2]
    start = 2
    print(compose(note, miscari, start))


main()
