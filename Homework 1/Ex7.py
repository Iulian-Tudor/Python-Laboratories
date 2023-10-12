def select_num(text):
    number = ""
    for i in range(len(text)):
        if text[i].isdigit():
            while i < len(text) and text[i].isdigit():
                number += text[i]
                i += 1
            break
    if not number:
        return "No numbers found."
    return int(number)


def main():
    sample = input("Enter sample text: ")
    print(select_num(sample))


main()
