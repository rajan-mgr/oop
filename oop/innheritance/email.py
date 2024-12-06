    # A base class User with private and protected attributes for name and email, along with public methods to access and modify email, and a public method to display user info.
    # A derived class Member that extends User, with additional private attributes to store a member ID and a list of borrowed books. Include methods for borrowing, returning, and displaying borrowed books. Limit the number of borrowed books to 5.
    # Another derived class Librarian that extends User, with private attributes for an employee ID. Include methods for adding and removing books from a library. These methods should take  the library object, and book to be added or removed. Note: we can pass the object of one class as an argument to the method of another class. 
    # A separate Library class with a protected attribute to store a list of books and methods to display available books.
    # Demonstrate the interaction between these classes by:
    #     Creating a Library object and adding books using a Librarian object.
    #     Allowing a Member to borrow and return books, and showing the borrowed books list.
    #     Updating the list of available books in the library after borrowing or returning.
    #     Displaying the details of users (Librarian and Member).

class User:
    def __init__(self, name, email):
        self.__name = name
        self._email = email

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def display_user_info(self):
        print(f"Name: {self.__name}, Email: {self._email}")


class Member(User):
    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.__member_id = member_id
        self.__borrowed_books = []

    def borrow_book(self, library, book):
        if len(self.__borrowed_books) < 5 and book in library.get_books():
            self.__borrowed_books.append(book)
            library.remove_book(book)
            print(f"Borrowed: {book}")
        elif book not in library.get_books():
            print(f"Book '{book}' is not available in the library.")
        else:
            print("Book borrowing limit reached (5 books).")

    def return_book(self, library, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            library.add_book(book)
            print(f"Returned: {book}")
        else:
            print(f"Book '{book}' is not in the borrowed books list.")

    def display_borrowed_books(self):
        if self.__borrowed_books:
            print("Borrowed Books:", ", ".join(self.__borrowed_books))
        else:
            print("No borrowed books.")


class Librarian(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.__employee_id = employee_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Added book: {book}")

    def remove_book(self, library, book):
        if book in library.get_books():
            library.remove_book(book)
            print(f"Removed book: {book}")
        else:
            print(f"Book '{book}' not found in the library.")


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def get_books(self):
        return self._books

    def display_books(self):
        if self._books:
            print("Available Books:", ", ".join(self._books))
        else:
            print("No books available in the library.")


# Demonstrating interaction
library = Library()
librarian = Librarian("Smriti Sharma", "smriti@example.com", "EMP001")
member = Member("Rajesh Magar", "rajesh@example.com", "MEM001")

# Librarian adds books to the library
librarian.add_book(library, "Shriman Kabir")
librarian.add_book(library, "Palpasa Cafe")
librarian.add_book(library, "Samjhanaka Khandaharu")

# Display available books
library.display_books()

# Member borrows books
member.borrow_book(library, "Palpasa Cafe")
member.borrow_book(library, "Shriman Kabir")
library.display_books()  # Available books should update
member.display_borrowed_books()

# Member returns a book
member.return_book(library, "Palpasa Cafe")
library.display_books()
member.display_borrowed_books()

# Display user details
librarian.display_user_info()
member.display_user_info()

  
    
                 
        
        
            