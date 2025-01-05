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
