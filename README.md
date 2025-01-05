# Library Management System

The **Library Management System** is a Python-based desktop application designed for managing books in a library. It offers a user-friendly interface using `Tkinter` and leverages `SQLite3` for data storage. The system allows users to add, view, search, update, and delete book records efficiently.

## Demonstration

Watch the project demonstration on YouTube:  
[![Library Management System](https://img.youtube.com/vi/GviKh5Z56YA/0.jpg)](https://youtu.be/GviKh5Z56YA)

## GitHub Repository

Access the source code on GitHub:  
[Library Management Repository](https://github.com/Maryam-tli/library_management.git)

## Features

- **Add Book**: Add new books with details like title, author, and publication year.
- **Display Books**: View all books stored in the database.
- **Search Books**: Search for books by title or author.
- **Update Book**: Update existing book records.
- **Remove Book**: Delete books by their unique ID.
- **Generate Report**: Create a summary of the library's collection.

## Project Structure

```plaintext
.
├── project.py         # Main application code
├── test_project.py    # Unit tests for the application
├── library.db         # SQLite database (generated automatically)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Maryam-tli/library_management.git
   ```
2. Navigate to the project directory:
   ```bash
   cd library_management
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Create a `requirements.txt` if needed, e.g., including `tkinter` for GUI development.)*

## How to Run

1. Open a terminal in the project directory.
2. Run the application:
   ```bash
   python project.py
   ```
3. Interact with the library management system through the graphical interface.

## Unit Testing

The project includes comprehensive unit tests to ensure functionality. To run tests:
```bash
python -m unittest test_project.py
```

## Screenshots

*(Optional: Add images of the application interface.)*

## How It Works

1. **Initialize Database**: The application initializes an SQLite database named `library.db` with a `books` table if it doesn't already exist.
2. **CRUD Operations**: Users can perform Create, Read, Update, and Delete operations via the GUI buttons.
3. **Report Generation**: Provides insights such as the total number of books, distribution by author, and publication year.

## Code Highlights

- **Database Initialization**:
   ```python
   def initialize_database(db_path="library.db"):
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
   ```
- **Add Book Logic**:
   ```python
   def add_book(db_path="library.db"):
       title = simpledialog.askstring("Add Book", "Enter the book title:")
       ...
       cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
   ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any features or bug fixes.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
