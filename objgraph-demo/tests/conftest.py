import pytest
from bookstore import Book, LeakyBook


@pytest.fixture(scope='session',
                params=[(Book, 'Book'), (LeakyBook, 'LeakyBook')])
def book_fixture(request):
    return request.param
