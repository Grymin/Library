import sqlite3

CREATE_READERS_TABLE = """CREATE TABLE IF NOT EXISTS readers (
    reader_id INTEGER PRIMARY KEY,
    reader_name TEXT,
    reader_surname TEXT
);"""

CREATE_BOOKS_TABLE = """CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    author_name TEXT,
    book_title TEXT
);"""

CREATE_READS_TABLE = """CREATE TABLE IF NOT EXISTS reads (
    read_id INTEGER PRIMARY KEY,
    book_id INTEGER,
    reader_id INTEGER
);"""

ADD_READER = "INSERT INTO readers (reader_name, reader_surname) VALUES (?, ?);"
ADD_AUTHOR = "INSERT INTO authors (author_name, author_surname) VALUES (?, ?);"
ADD_BOOK = "INSERT INTO books (author_name, book_title) VALUES (?, ?);"
ADD_READ = "INSERT INTO reads (book_id, reader_id) VALUES (?, ?);"

GET_BOOK_ID = "SELECT book_id FROM books WHERE book_title=?;"
GET_READER_ID = "SELECT reader_id FROM readers WHERE reader_name=? AND reader_surname=?"

CHECK_READER = "SELECT COUNT(*) FROM readers WHERE reader_name=? AND reader_surname=?;"

DELETE_READER = "DELETE FROM readers WHERE reader_name=? AND reader_surname=?;"
DELETE_READ = "DELETE FROM reads WHERE read_id=?"

VIEW_READERS = "SELECT * FROM readers;"
VIEW_BOOKS_ALL = "SELECT * FROM books;"
VIEW_READS = """
SELECT
    reads.read_id,
    books.book_title, 
    readers.reader_name,
    readers.reader_surname
FROM reads
JOIN books ON reads.book_id = books.book_id
JOIN readers ON readers.reader_id = reads.reader_id
"""
VIEW_BOOKS_READER = """
SELECT 
    books.book_title
FROM reads 
JOIN books ON books.book_id = reads.book_id
JOIN readers ON readers.reader_id = reads_reader_id
WHERE reader.reader_name = ? AND reader.reader_surname=?"
);"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_BOOKS_TABLE)
        connection.execute(CREATE_READERS_TABLE)
        connection.execute(CREATE_READS_TABLE)


def get_book_id(book_title):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_BOOK_ID, (book_title,))
        return cursor.fetchone()


def get_reader_id(reader_name, reader_surname):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_READER_ID, (reader_name, reader_surname,))
        return cursor.fetchone()


def add_reader(name, surname):
    with connection:
        connection.execute(ADD_READER, (name, surname,))


def add_book(author_name, book_title):
    with connection:
        connection.execute(ADD_BOOK, (author_name, book_title,))


def add_read(book_title, reader_name, reader_surname):
    book_id = get_book_id(book_title)[0]
    reader_id = get_reader_id(reader_name, reader_surname)[0]
    print('ID wartosci', book_id, reader_id)
    with connection:
        connection.execute(ADD_READ, (book_id, reader_id))


def check_reader(name, surname):
    with connection:
        cursor = connection.cursor()
        cursor.execute(CHECK_READER, (name, surname,))
        return cursor.fetchone()


def delete_reader(name, surname):
    with connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_READER, (name, surname,))


def delete_read(read_id):
    with connection:
        connection.execute(DELETE_READ, (read_id,))


def view_readers():
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_READERS)
        return cursor.fetchall()


def view_reads():
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_READS)
        return cursor.fetchall()


def view_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_BOOKS_ALL)
        return cursor.fetchall()


def view_books_reader(name, surname):
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_BOOKS_READER, (name, surname,))
        return cursor.fetchall()