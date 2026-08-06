#Q. Library Management System (Constructor & Inheritance)
#A library stores information about books and digital books. Create a base class Book with a constructor to initialize book details.
#Create a derived class EBook that adds file size information.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book Title :", self.title)
        print("Author     :", self.author)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        super().display()
        print("File Size  :", self.file_size, "MB")

ebook = EBook("Iam you", "John", 15)

ebook.display()
