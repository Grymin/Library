import datetime

import database

welcome = "Welcome to the house library!"

menu = """Choose option:
1) Add reader
2) Delete reader
3) View readers
4) Add book
5) View all books
6) Add read
7) Delete read
8) View reads
0) Exit

Your selection: """

print(welcome)

database.create_tables()


def prompt_add_reader():
    name = input("Reader's name:")
    surname = input("Reader's surname:")
    database.add_reader(name, surname)
    print(f"Reader {name} {surname} added successfully")


def prompt_add_book():
    author = input("Author name:")
    title = input("Book title:")
    database.add_book(author, title)
    print(f"Book {title} by {author} added successfully")


def delete_reader():
    name = input("Name to delete:")
    surname = input("Surname to delete:")
    checker = database.check_reader(name, surname)[0]
    if checker:
        database.delete_reader(name, surname)
        print(f"Reader {name} {surname} deleted successfully!")
    else:
        print("Such a reader does not exist!")


def delete_read():
    print('Current reads:')
    view_reads()
    num_to_del = input("Give index of read to delete:")
    database.delete_read(num_to_del)


def view_readers():
    readers = database.view_readers()
    for (pos, name, surname) in readers:
        print(f'{pos}: {name} {surname}')


def view_reads():
    reads = database.view_reads()
    for pos, title, name, surname in reads:
        print(f'{pos}:\n\tTITLE: {title}\n\tNAME: {name}\n\tSURNAME: {surname}\n')


def view_books():
    books = database.view_books()
    for (pos, author, title) in books:
        print(f'{pos}:\n\tAUTHOR: {author}\n\tTITLE: {title}')


def add_read():
    book = input("book title:")
    reader_name = input("reader name:")
    reader_surname = input("reader surname:")
    database.add_read(book, reader_name, reader_surname)


def view_books_reader():
    name = input("Name of reader:")
    surname = input("Surname of reader:")
    books_by_reader = database.view_books_reader(name, surname)
    print(books_by_reader)


while (choice := input(menu)) != 8:
    if choice == '1':
        prompt_add_reader()
    elif choice == '2':
        delete_reader()
    elif choice == '3':
        view_readers()
    elif choice == '4':
        prompt_add_book()
    elif choice == '5':
        view_books()
    elif choice == '6':
        add_read()
    elif choice == '7':
        delete_read()
    elif choice == '8':
        view_reads()
    else:
        print('Wrong value')
