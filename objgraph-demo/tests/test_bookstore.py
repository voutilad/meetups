#!/bin/env python
import gc
import objgraph
from io import StringIO

from bookstore import Book, Page


def test_building_a_book(booktype):
    """
    Can we create a new Book and add some Page's?
    :return: None
    """

    book = booktype(title='The Hobbit')
    assert book.title == 'The Hobbit'
    assert book.pages == []

    page = Page(text='This is page 1!')
    assert page.text == 'This is page 1!'

    book.append(page)
    assert book.pages == [page]
    assert len(book) == 1


def test_garbage_collection(booktype):
    """
    Build a Book and see if it gets garbage collected
    :return: None
    """

    # we'll use this to collect output from objgraph
    stdout = StringIO()

    # initialize objgraph's tracking, run it 3 times to get through
    # dynamic loading of things
    print('')
    objgraph.show_growth(file=stdout)
    objgraph.show_growth(file=stdout)
    objgraph.show_growth(file=stdout)

    book = Book(title='Total Garbage')
    book.append(Page(text='This is page 1'))
    book.append(Page(text='This is page 2'))

    # look for growth
    print('Growth:\n')
    objgraph.show_growth()

    # let's destroy our book
    print('\nBurning our book!')
    del book
    gc.collect()

    # look for shrinkage
    print('\nMake sure nothing is left.')
    books = objgraph.by_type('Book')
    print('books == ' + str(books))
    assert books == []
