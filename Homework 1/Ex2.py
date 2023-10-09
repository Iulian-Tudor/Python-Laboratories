

def main():
    prop = "This is a test for exercise 2"
    count = 0
    vowels = {"a", "o", "i", "u", "e"}

    for i in range(len(prop)):
        if prop[i] in vowels:
            count += 1

    print(count)


main()
