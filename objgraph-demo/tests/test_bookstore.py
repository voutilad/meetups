#!/bin/env python
import gc
import objgraph
from io import StringIO

from bookstore import Book, Page


def test_building_a_book(book_fixture):
    """
    Can we create a new Book and add some Page's?
    :return: None
    """
    booktype = book_fixture[0]
    book = booktype(title='The Hobbit')
    assert book.title == 'The Hobbit'
    assert book.pages == []

    page = Page(text='This is page 1!')
    assert page.text == 'This is page 1!'

    book.append(page)
    assert book.pages == [page]
    assert len(book) == 1

    book.append(Page('This is page 2!'))
    assert book.pages[-1].text == 'This is page 2!'
    assert len(book) == 2


def test_garbage_collection(book_fixture):
    """
    Build a Book and see if it gets garbage collected
    :return: None
    """
    booktype = book_fixture[0]
    bookclass = book_fixture[1]

    # we'll use this to collect output from objgraph
    stdout = StringIO()

    # initialize objgraph's tracking, run it 3 times to get through
    # dynamic loading of things
    print('')
    objgraph.show_growth(file=stdout)
    objgraph.show_growth(file=stdout)
    objgraph.show_growth(file=stdout)

    book = booktype(title='Total Garbage')
    book.append(Page('This is page 1'))
    book.append(Page('This is page 2'))

    # look for growth
    print('\n Growth:\n')
    objgraph.show_growth()

    # let's destroy our book
    print('\n Burning our book!')
    del book
    gc.collect()

    # not even ashes should remain!
    print('\n Make sure nothing is left.')
    books = objgraph.by_type(bookclass)
    print(bookclass + ' == ' + str(books))
    assert books == []


