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
