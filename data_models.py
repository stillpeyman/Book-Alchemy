from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Author(db.Model):
    """
    Represents an author in the library database.

    Attributes:
        id (int): Primary key, auto-incremented.
        name (str): Full name of the author. Cannot be null.
        birth_date (date): Date of birth of the author.
        date_of_death (date): Date of death of the author, if applicable.
    """
    __tablename__ = 'Author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    birth_date = db.Column(db.String)
    date_of_death = db.Column(db.String)

    def __repr__(self):
        """
        Returns a string that represents the object for debugging.

        Example:
            Author(id = 1, name = 'George Orwell')
        """
        return f"Author(id = {self.id}, name = {self.name})"
    
    def __str__(self):
        """
        Returns a human-readable string representation of the author.

        Example:
            'George Orwell (1903-06-25 - 1950-01-21)'
        """
        return f"{self.name} ({self.birth_date} - {self.date_of_death})"


class Book(db.Model):
    """
    Represents a book in the library database.

    Attributes:
        id (int): Primary key, auto-incremented.
        isbn (str): International Standard Book Number. Cannot be null.
        title (str): Title of the book. Cannot be null.
        publication_year (int): Year the book was published.
        author_id (int): Foreign key referencing the author's ID.
    """
    __tablename__ = 'Book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('Author.id'))

    # Create a relationship property called 'author'
    # Get access to all properties of Author object
    author = db.relationship('Author')

    def __repr__(self):
        """
        Returns a string that represents the object for debugging.

        Example:
            Book(id = 1, title = '1984')
        """
        return f"Book(id = {self.id}, title = {self.title})"
    
    def __str__(self):
        """
        Returns a human-readable string representation of the book.

        Example:
            '1984 (1949)'
        """
        return f"{self.title} ({self.publication_year})"
