class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print(f'"{title}" has been added to the library.')

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")

    def borrow_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f'You have borrowed "{title}".')
        else:
            print(f'Sorry, "{title}" is not available.')

    def return_book(self, title):
        self.books.append(title)
        print(f'Thank you for returning "{title}".')


# Main program
def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the book title to add: ")
            library.add_book(title)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter the book title to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter the book title to return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
