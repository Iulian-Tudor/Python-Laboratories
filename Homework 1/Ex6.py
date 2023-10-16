def is_palindrome(text):
    return text == text[::-1]


def main():
    text = input("Enter what you want to check: ")
    print(type(text))
    if is_palindrome(text):
        print("This is a palindrome")
    else:
        print("This is NOT a palindrome")


main()
