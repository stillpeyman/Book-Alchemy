from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# directory of your app.py
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'library.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

# Connect Flask app to flask-sqlalchemy code
db.init_app(app)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    # Handle POST request
    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        date_of_death = request.form.get('date_of_death')

        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()

        flash(f"Author '{name}' added successfully!")
    
    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    # Handle POST request
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')

        new_book = Book(isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()

        flash(f"Book '{title}' added successfully!")
    
    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author = book.author

    # Delete the book
    db.session.delete(book)
    db.session.commit()

    # Check if author has any other books
    other_books = Book.query.filter_by(author_id=author.id).count()
    if other_books == 0:
        db.session.delete(author)
        db.session.commit()
    
    flash(f"Book '{book.title}' deleted successfully!")
    return redirect(url_for('index'))


@app.route('/')
def index():
    # Get search param from URL query string, default to empty string
    search_query = request.args.get('search', '').strip()

    # Get sort params from URL query string, default to 'title'
    sort = request.args.get('sort', 'title')

    if search_query:
        # Case-insensitive partial match
        books = Book.query.filter(Book.title.ilike(f'%{search_query}%')).all()

    elif sort == 'author':
        # Join with Author and order by author name
        books = Book.query.join(Author).order_by(Author.name).all()
    
    else:
        # Default sorting by book title
        books = Book.query.order_by(Book.title).all()

    # Render template and pass books and current sort for dropdown
    return render_template('home.html', books=books, sort=sort, search=search_query)


if __name__ == '__main__':
    # # Run <with> block once to create the tables in database
    # # Comment out after first run. Else, it might overwrite the setup
    # with app.app_context():
    #     db.create_all()
    app.run(host="0.0.0.0", port=5001, debug=True)