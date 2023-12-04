def max_freq(text):
    freq = 0
    result = ""
    text.lower()
    for i in text:
        if i.isalpha():
            if "a" <= i <= "z":
                count = text.count(i)
                if count > freq:
                    freq = count
                    result = i
    return result


def main():
    sample = input("Enter a string: ")
    print(max_freq(sample))


main()
