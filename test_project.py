import unittest
import sqlite3
import os
from unittest.mock import patch
from project import (
    initialize_database,
    add_book,
    display_books,
    remove_book,
    search_books,
    update_book,
    generate_report,
)


class TestLibraryManagement(unittest.TestCase):
    def setUp(self):
        """set up a temporary database for testing."""
        self.test_db = "test_library.db"
        initialize_database(self.test_db)

    def tearDown(self):
        """Remove the temporary database after tests."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_initialize_database(self):
        """Test if the database and table are initialized correctly."""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
        table_exists = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(table_exists, "Table 'books' should exist.")

    @patch('tkinter.simpledialog.askstring', side_effect=["Test Book", "Test Author"])
    @patch('tkinter.simpledialog.askinteger', return_value=2021)
    def test_add_book(self, mock_askinteger, mock_askstring):
        """Test adding a book."""
        add_book(self.test_db)
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title='Test Book'")
        book = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(book, "Book should be added to the database.")

    @patch('tkinter.simpledialog.askinteger', return_value=1)
    def test_remove_book(self, mock_askinteger):
        """Test removing a book."""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES ('Book1', 'Author1', 2021)")
        conn.commit()
        conn.close()

        remove_book(self.test_db)

        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id=1")
        book = cursor.fetchone()
        conn.close()
        self.assertIsNone(book, "Book should be removed from the database.")

    @patch('tkinter.simpledialog.askstring', return_value="Book1")
    def test_search_books(self, mock_askstring):
        """Test searching books."""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES ('Book1', 'Author1', 2021)")
        conn.commit()
        conn.close()

        with patch('tkinter.messagebox.showinfo') as mock_messagebox:
            search_books(self.test_db)
            mock_messagebox.assert_called_with(
                "Search Results", "ID: 1, Title: Book1, Author: Author1, Year: 2021"
            )

    @patch('tkinter.simpledialog.askinteger', side_effect=[1, 2022])
    @patch('tkinter.simpledialog.askstring', side_effect=["Updated Book", "Updated Author"])
    def test_update_book(self, mock_askstring, mock_askinteger):
        """Test updating a book."""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES ('Book1', 'Author1', 2021)")
        conn.commit()
        conn.close()

        update_book(self.test_db)

        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id=1")
        book = cursor.fetchone()
        conn.close()

        # Assertions for updated book
        self.assertEqual(book[1], "Updated Book", "Book title should be updated.")
        self.assertEqual(book[2], "Updated Author", "Book author should be updated.")
        self.assertEqual(book[3], 2022, "Book year should be updated.")

    def test_generate_report(self):
        """Test generating report."""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            [
                ('Book1', 'Author1', 2021),
                ('Book2', 'Author1', 2022),
                ('Book3', 'Author2', 2021),
            ],
        )
        conn.commit()
        conn.close()

        with patch('tkinter.messagebox.showinfo') as mock_messagebox:
            generate_report(self.test_db)
            report = (
                "Total books: 3\n\nBooks by Author:\nAuthor1: 2\nAuthor2: 1\n\nBooks by Year:\n2021: 2\n2022: 1\n"
            )
            mock_messagebox.assert_called_with("Library Report", report)

    def test_display_books(self):
        """Test displaying books."""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES ('Book1', 'Author1', 2021)")
        conn.commit()
        conn.close()

        with patch('tkinter.messagebox.showinfo') as mock_messagebox:
            display_books(self.test_db)
            mock_messagebox.assert_called_with(
                "Library Collection", "ID: 1, Title: Book1, Author: Author1, Year: 2021"
            )


if __name__ == "__main__":
    unittest.main()
