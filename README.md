# Flask Library Management

A simple Flask app to manage authors and books using SQLite and SQLAlchemy.

## Features

- Add and delete authors
- Add and delete books
- Search and sort books
- Automatically remove authors with no books

## Setup

1. **Clone the repo and install dependencies**
    ```
    git clone https://github.com/stillpeyman/Book-Alchemy.git

    cd BOOK-ALCHEMY

    pip install flask flask-sqlalchemy python-dotenv
    ```

2. **Set up environment**

    - Flask's SECRET_KEY is required for using flash().
    - Create a `.env` file with:
      ```
      SECRET_KEY=choose-your-own-secret-key
      ```

3. **Initialize the database (first run only)**
    - Uncomment the `db.create_all()` block in `app.py`
    - Run:
      ```
      python3 app.py
      ```
    - Comment the block again after tables are created.

4. **Run the app**
    ```
    python app.py
    ```
    By default, visit [http://localhost:5001](http://localhost:5001)

    If you change the port in `app.py`, use the corresponding port (e.g., 5002).

## Main Routes

- `/` — Home (list, search, sort books)
- `/add_author` — Add an author
- `/add_book` — Add a book

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.