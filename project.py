import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog


def initialize_database(db_path="library.db"):
    """Initialize the SQLite database and create the books table if it doesn't exist."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_book(db_path="library.db"):
    """Add a new book to the database."""
    title = simpledialog.askstring("Add Book", "Enter the book title:")
    if not title:
        return
    author = simpledialog.askstring("Add Book", "Enter the author:")
    if not author:
        return
    year = simpledialog.askinteger("Add Book", "Enter the year of publication:")
    if not year:
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Book '{title}' added successfully.")


def display_books(db_path="library.db"):
    """Display all books in the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    conn.close()

    if results:
        books = "\n".join([f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}" for row in results])
        messagebox.showinfo("Library Collection", books)
    else:
        messagebox.showinfo("Library Collection", "The library is empty.")


def remove_book(db_path="library.db"):
    """Remove a book from the database."""
    book_id = simpledialog.askinteger("Remove Book", "Enter the ID of the book to remove:")
    if not book_id:
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Book with ID {book_id} removed successfully.")


def search_books(db_path="library.db"):
    """Search for books by title or author."""
    query = simpledialog.askstring("Search Books", "Enter the title or author to search for:")
    if not query:
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()
    conn.close()

    if results:
        books = "\n".join([f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}" for row in results])
        messagebox.showinfo("Search Results", books)
    else:
        messagebox.showinfo("Search Results", "No books found matching the query.")


def update_book(db_path="library.db"):
    """Update an existing book's information."""
    book_id = simpledialog.askinteger("Update Book", "Enter the ID of the book to update:")
    if not book_id:
        return

    new_title = simpledialog.askstring("Update Book", "Enter the new title (leave blank to keep current):")
    new_author = simpledialog.askstring("Update Book", "Enter the new author (leave blank to keep current):")
    new_year = simpledialog.askinteger("Update Book", "Enter the new year (leave blank to keep current):")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if new_title:
        cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
    if new_author:
        cursor.execute("UPDATE books SET author = ? WHERE id = ?", (new_author, book_id))
    if new_year:
        cursor.execute("UPDATE books SET year = ? WHERE id = ?", (new_year, book_id))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Book with ID {book_id} updated successfully.")


def generate_report(db_path="library.db"):
    """Generate a report of the library's content."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    cursor.execute("SELECT author, COUNT(*) FROM books GROUP BY author")
    books_by_author = cursor.fetchall()

    cursor.execute("SELECT year, COUNT(*) FROM books GROUP BY year")
    books_by_year = cursor.fetchall()

    conn.close()

    report = f"Total books: {total_books}\n\nBooks by Author:\n"
    for author, count in books_by_author:
        report += f"{author}: {count}\n"
    report += "\nBooks by Year:\n"
    for year, count in books_by_year:
        report += f"{year}: {count}\n"

    messagebox.showinfo("Library Report", report)


def main():
    db_path = "library.db"  # Change this path for testing if needed
    initialize_database(db_path)

    root = tk.Tk()
    root.title("Library Management System")

    tk.Button(root, text="Add Book", command=lambda: add_book(db_path), width=20).pack(pady=5)
    tk.Button(root, text="Display Books", command=lambda: display_books(db_path), width=20).pack(pady=5)
    tk.Button(root, text="Remove Book", command=lambda: remove_book(db_path), width=20).pack(pady=5)
    tk.Button(root, text="Search Books", command=lambda: search_books(db_path), width=20).pack(pady=5)
    tk.Button(root, text="Update Book", command=lambda: update_book(db_path), width=20).pack(pady=5)
    tk.Button(root, text="Generate Report", command=lambda: generate_report(db_path), width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
