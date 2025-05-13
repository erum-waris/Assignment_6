# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0 # Class variable to keep track of the total number of books

      # adding a new book using constructor
    def __init__(self, book_name):
        self.book_name = book_name
        Book.increment_book_count()
        print(f"Book added: {self.book_name}")
        
    @classmethod 
    def increment_book_count(cls):  # cls is a reference to the class itself we can any ther name but recommended cls best practice
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")
       

    # adding a new book using constructor
    def __init__(self, book_name):
        self.book_name = book_name
        Book.increment_book_count()
        print(f"Book added: {self.book_name}")

# Creating instances of Book
book1 = Book("Python Programming")
book2 = Book("Data Science with Python")
book3 = Book("Machine Learning with Python")
book4 = Book("Deep Learning with Python")
book5 = Book("Artificial Intelligence with Python")


