from src.controllers import BookController


def setup_routes(app):
    app.add_route(BookController.as_view(), '/api/books')
