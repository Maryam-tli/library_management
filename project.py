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
