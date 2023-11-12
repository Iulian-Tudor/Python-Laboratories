class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_item(self):
        self.checked_out = False

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Checked out: {self.checked_out}")


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def display(self):
        super().display()
        print(f"Pages: {self.pages}")


class DVD(LibraryItem):
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def display(self):
        super().display()
        print(f"Length: {self.duration}")


class Magazine(LibraryItem):
    def __init__(self, title, author, year, number):
        super().__init__(title, author, year)
        self.number = number

    def display(self):
        super().display()
        print(f"Number: {self.number}")


def main():
    book = Book("The Grapes of Wrath", "John Steinbeck", 1939, 464)
    dvd = DVD("The Godfather", "Francis Ford Coppola", 1972, 175)
    magazine = Magazine("National Geographic", "National Geographic Society", 1888, 1)

    book.display()
    print()
    dvd.display()
    print()
    magazine.display()
    print()
    magazine.check_out()
    magazine.display()


main()
