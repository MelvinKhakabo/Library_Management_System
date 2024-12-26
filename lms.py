class Book:
    def __init__(self, Book_title, Book_author, IS_Book_number):
        self.Book_title = Book_title
        self.Book_author = Book_author
        self.IS_Book_number= IS_Book_number
        self.is_available = True

    def displayinfo(self):
        print(f"Title: {self.Book_title}\nAuthor: {self.Book_author}\nIS_Book_Number: {self.IS_Book_number}\nAvailable: {self.is_available}\n")