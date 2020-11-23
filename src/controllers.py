
from sanic.response import json
from sanic.views import HTTPMethodView

from src.models import Book


class BookController(HTTPMethodView):
    """ Handles Book CRUD operations using Sanic Class based views. """

    async def get(self, request):
        """ Gets all books in the DB
         Args:
             request (object): contains data pertaining request.
         Notes:
             Realistically There would be some form of authentication in place
             Like a Token to grab the Auth Header value and return a specific
             user based on Token. Although for the purpose of brevity this route
             will just return all users in the database.
         Returns:
             json: containing list of users under the `users` key.
         """
        query = Book.__table__.select()
        rows = await request.app.db.fetch_all(query)
        return json({
            "books": [{row["title"]: row["author"]} for row in rows]
        })

    async def post(self, request):
        """ Creates a new book based on the `title` & `author` keys.
        Args:
            request (object): contains data pertaining request.
        Returns:
            json: containing key `msg` with success info & full title.
        """
        title = request.json.get('title')
        author = request.json.get('author')

        book = Book(title=title, author=author)
        query = Book.__table__.insert()
        values = {"title": title, "author": author}
        db = request.app.db
        await db.execute(query=query, values=values)

        return json(
            {"msg": "Successfully created '{}'".format(book.full_title())}
        )
