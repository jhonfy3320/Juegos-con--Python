class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'El libro "{self.title}" ha sido prestado')
        else:
            print(f'El libro "{self.title}" no está disponible')

    def return_book(self):
        self.available = True
        print(f'El libro "{self.title}" ha sido devuelto')

class User:
    def __init__(self, name, user_id) -> None:
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro "{book.title}" no está disponible')
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'El libro "{book.title}" no está en la lista de prestados')

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f'El libro "{book.title}" ha sido agregado')

    def register_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido registrado')

    def show_available_books(self):
        print('Libros disponibles:')
        for book in self.books:
            if book.available:
                print(f'"{book.title}" por {book.author}')

# Creando libros 
Book_1 = Book("Cien años de soledad", 'Gabriel García Márquez')
Book_2 = Book("1984", 'George Orwell')
Book_3 = Book("El nombre de la rosa", 'Umberto Eco')
Book_4 = Book("Orgullo y prejuicio", "Jane Austen")
Book_5 = Book("El señor de los anillos", "J.R.R. Tolkien")
Book_6 = Book("Crimen y castigo", 'Fyodor Dostoevsky')
Book_7 = Book("Matar a un ruiseñor", 'Harper Lee')
Book_8 = Book("Don Quijote de la Mancha", 'Miguel de Cervantes')
Book_9 = Book("La metamorfosis", 'Franz Kafka')
Book_10 = Book("Ulises", 'James Joyce')

# Creando usuarios
User1 = User('Nico', '001')
User2 = User('Alejandro', '002')
User3 = User('Emanuel', '003')
User4 = User('Freddy', '004')

# Creando la biblioteca
library = Library()
library.add_book(Book_1)
library.add_book(Book_2)
library.add_book(Book_3)
library.add_book(Book_4)
library.add_book(Book_5)
library.add_book(Book_6)
library.add_book(Book_7)
library.add_book(Book_8)
library.add_book(Book_9)
library.add_book(Book_10)
library.register_user(User1)
library.register_user(User2)
library.register_user(User3)
library.register_user(User4)

# Mostrar libros disponibles
library.show_available_books()

# Realizar préstamo
User1.borrow_book(Book_1)
User2.borrow_book(Book_4)
User3.borrow_book(Book_10)
User4.borrow_book(Book_3)

# Mostrar libros disponibles después de los préstamos
library.show_available_books()

# Devolver libro
User1.return_book(Book_1)

# Mostrar libros disponibles después de la devolución
library.show_available_books()
