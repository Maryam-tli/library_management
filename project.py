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
