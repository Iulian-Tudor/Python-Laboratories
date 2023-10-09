
def change_case(word):
    final = [word[0].lower()]
    for c in word[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            final.append('_')
            final.append(c.lower())
        else:
            final.append(c)

    return ''.join(final)


def main():
    word = input("Enter a string: ")
    print(change_case(word))

main()