from enum import Enum

class BookStatus(Enum):
	AVAILABLE = "available"
	BORROWED = "borrowed"

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.status = BookStatus.AVAILABLE

	def borrow_book(self):
		if self.status == BookStatus.AVAILABLE:
			self.status = BookStatus.BORROWED
			return True
		return False

	def return_book(self):
		if self.status == BookStatus.BORROWED:
			self.status = BookStatus.AVAILABLE
			return True
		return False

	def __str__(self):
		return f"'{self.title}' by {self.author} - Status: {self.status.value}"

class Library:
	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def borrow_book(self, title):
		for book in self.books:
			if book.title == title:
				if book.borrow_book():
					print(f"You have borrowed '{title}'.")
					return
				else:
					print(f"'{title}' is currently unavailable.")
					return
		print(f"Book '{title}' not found in the library.")
	
	def return_book(self, title):
		for book in self.books:
			if book.title == title:
				if book.return_book():
					print(f"You have returned '{title}'.")
					return
				else:
					print(f"'{title}' was not borrowed.")
					return
		print(f"Book '{title}' not found in the library.")

	def list_available(self):
		for book in self.books: 
			if book.status == BookStatus.AVAILABLE:
				print(book)

book_list = [
	Book("1984", "George Orwell"),
	Book("To Kill a Mockingbird", "Harper Lee"),
	Book("The Great Gatsby", "F. Scott Fitzgerald"),
]
library = Library()
for book in book_list:
	library.add_book(book)
library.list_available()
library.borrow_book("1984")
library.list_available()
library.return_book("1984")
library.list_available()