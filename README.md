📚 Library Management System (Python, Tkinter, SQLite & MySQL)

A simple and beginner-friendly Library Management System built using Python, Tkinter, SQLite, and MySQL.
This project demonstrates GUI development + CRUD operations + database integration for both local (SQLite) and server-based (MySQL) databases.

⭐ Features

- Add new books

- View all books

- Search books by title/author/year/ISBN

- Edit/Update books

- Delete books

- Clean and formatted list display

- Supports two database backends: SQLite and MySQL

🛠 Technologies Used

- Python

- Tkinter

- SQLite

- MySQL

- mysql-connector-python

- PyCharm IDE

🔌 Database Versions Supported
1️⃣ SQLite Version (Default)

- Backend file: backend.py

- Database file: library.db (auto-created)

- No installation required

To enable SQLite backend, in frontend.py use:

  import backend as backend

2️⃣ MySQL Version

- Backend file: backend_mysql.py

- Requires MySQL Server & Workbench

- Uses mysql-connector-python

MySQL Setup Commands (Run in Workbench)
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

CREATE TABLE IF NOT EXISTS books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT,
    isbn VARCHAR(50)
);

Update MySQL Credentials

In backend_mysql.py:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "library_db"
}


To enable MySQL backend, in frontend.py use:

  import backend_mysql as backend

▶️ How to Run

1. Download or clone the project

2. (MySQL Version Only) Install MySQL connector:

   pip install mysql-connector-python

3. Run the Tkinter application:

   python frontend.py

📁 Project Structure
backend.py          → SQLite backend
backend_mysql.py    → MySQL backend
frontend.py         → Tkinter GUI
library.db          → SQLite database
README.md           → Documentation
LICENSE             → License file

🚀 Future Enhancements

- Login system

- Issue/return book feature

- Better UI using CustomTkinter

- Export data to Excel

- MySQL cloud database version (online DB)

- Pagination for long book lists

📜 License

This project is open-source under the MIT License.
