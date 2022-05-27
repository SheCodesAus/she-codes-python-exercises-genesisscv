class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


my_book = Book("A great book", "me")
print(my_book)
