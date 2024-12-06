class LibraryMember:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)
        print(f"{self.name} has borrowed '{book_title}'.")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f"{self.name} has returned '{book_title}'.")
        else:
            print(f"{self.name} did not borrow '{book_title}'.")


class StudentMember(LibraryMember):
    def __init__(self, name, membership_id, student_id):
        super().__init__(name, membership_id)
        self.student_id = student_id

    def borrow_book(self, book_title):
        print(f"Student {self.name} (ID: {self.student_id}) is borrowing a book.")
        super().borrow_book(book_title)

    def access_study_room(self):
        print(f"{self.name} has accessed the study room.")


# Example usage
generic_member = LibraryMember("Sita", "M001")
generic_member.borrow_book("Dreamers")
generic_member.return_book("Dreamers")

student_member = StudentMember("Ram", "M002", "S123")
student_member.borrow_book("Grievance")
student_member.return_book("Grievance")
student_member.access_study_room()
