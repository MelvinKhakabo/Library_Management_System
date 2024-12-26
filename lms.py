#Create a Book Class and initialize the parameters using Constructor
class Book:
    def __init__(self, Book_title, Book_author, IS_Book_number):
        self.Book_title = Book_title
        self.Book_author = Book_author
        self.IS_Book_number= IS_Book_number
        self.is_available = True

    def displayinfo(self):
        print(f"Title: {self.Book_title}\nAuthor: {self.Book_author}\nIS_Book_Number: {self.IS_Book_number}\nAvailable: {self.is_available}\n")

#Assign books to keep in the library list
x = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
y = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-0")
z = Book("Pride and Prejudice", "Jane Austen", "978-0-06-112008-0")
 
x.displayinfo()
y.displayinfo()
z.displayinfo() 

#Create a Library Class by initializing the parameters and adding methods
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self. books.append(book)
        print(f"Book '{book.Book_title}' added to the library.")

    def display_books(self):
        print("List of Library Books:")
        for i in self.books:
            i.display_info()

    def lend_book(self, Book_title):
        for j in self.books:
            if j.Book_title == Book_title and j.is_available:
                j.is_available = False
                print(f"Book '{Book_title}' has been lent.")
                return
        print(f"Sorry, '{Book_title}' is either not available or does not exist in the library.")

    def return_book(self, Book_title):
        for k in self.books:
            if k.Book_title == Book_title and not k.is_available:
                k.is_available = True
                print(f"Book '{Book_title}' has been returned.")
                return
        print(f"Sorry, '{Book_title}' cannot be returned. Check the book title or availability.")
    def available_books(self):
        return [book for book in self.books if book.is_available]

    def display_current_books(self):
        current_books = self.available_books()
        if not current_books:
            print("No books currently available in the library.")
        else:
            print("\nCurrent Books in the Library:")
            for book in current_books:
                book.display_info()
