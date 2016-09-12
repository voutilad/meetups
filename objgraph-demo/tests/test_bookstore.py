#!/bin/env python
from bookstore import Book, Page


def test_building_a_book():
    """
    Can we create a new Book and add some Page's?
    :return: None
    """

    book = Book(title='The Hobbit')
    assert book.title == 'The Hobbit'
    assert book.pages == []

    page = Page(text='This is page 1!')
    assert page.text == 'This is page 1!'

    book.append(page)
    assert book.pages == [page]
    assert len(book) == 1
