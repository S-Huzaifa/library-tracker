# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}

def add_book():
    title = input("Title: ")
    author = input("Author: ")

    if title in books:
        print(f'"{title}" is already in the library.')
    else:
        books[title] = {
            "author": author,
            "available": True
        }
        print(f'Added "{title}".')
def list_books():
    if not books:
        print("No books in the library.")
        return

    for title, details in books.items():
        status = "Available" if details["available"] else "Borrowed"
        print(f'{title} by {details["author"]} - {status}')

def return_book():
    title = input("Title: ")

    if title not in books:
        print(f'No book titled "{title}".')
    elif books[title]["available"]:
        print(f'"{title}" is not borrowed.')
    else:
        books[title]["available"] = True
        print(f'You returned "{title}".')

def borrow_book():
    title = input("Title: ")

    if title not in books:
        print(f'No book titled "{title}".')
    elif not books[title]["available"]:
        print(f'"{title}" is already borrowed.')
    else:
        books[title]["available"] = False
        print(f'You borrowed "{title}".')

print("1. Add book")
print("2. List books")
print("3. Borrow book")
print("4. Return book")
print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            add_book()
        elif choice == "2":
            list_books()

        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()