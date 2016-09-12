import pytest
from bookstore import Book, LeakyBook


@pytest.fixture(scope='session', params=[Book, LeakyBook])
def booktype(request):
    return request.param
