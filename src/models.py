
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(length=100), nullable=True)
    author = Column(String(length=100), nullable=True)
    is_active = Column(Boolean, default=False)

    def __repr__(self):
        """Show object info."""
        return f"<Book: {self.id}>"

    def full_title(self):
        """Return title & author as a string."""
        return f"{self.title} by {self.author}"
