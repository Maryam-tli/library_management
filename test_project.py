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

    @patch('tkinter.simple dialog.askstring', side_effect=["Test Book", "Test Author"])
    @patch('tkinter.simple dialog.askinteger', return_value=2021)
    def test_add_book(self, mock_askinteger, mock_askstring):
        """Test adding a book."""
        add_book(self.test_db)
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title='Test Book'")
        book = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(book, "Book should be added to the database.")
