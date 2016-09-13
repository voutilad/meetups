import pytest
from bookstore import Book, LeakyBook
from bookstore.storage import _pages


@pytest.fixture(scope='session',
                params=[(Book, 'Book'), (LeakyBook, 'LeakyBook')])
def book_fixture(request):
    return request.param


@pytest.fixture(autouse=True)
def clear_pages():
    _pages.clear()
