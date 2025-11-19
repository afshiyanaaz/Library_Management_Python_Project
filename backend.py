import sqlite3

def connect():
    """Create database and table if not exists"""
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER,
            isbn TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    """Insert a new book"""
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    """Return all books"""
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    """Search for books by given fields"""
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM book
        WHERE title LIKE ? AND author LIKE ? AND
              (year = ? OR ? = '') AND
              (isbn = ? OR ? = '')
    """, ('%' + title + '%', '%' + author + '%', year, year, isbn, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    """Delete book by id"""
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    """Update book by id"""
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE book
        SET title = ?, author = ?, year = ?, isbn = ?
        WHERE id = ?
    """, (title, author, year, isbn, id))
    conn.commit()
    conn.close()


# Ensure table is created when backend is imported
connect()
