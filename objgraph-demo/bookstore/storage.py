"""
Dumb fake abstracted away storage
"""
import collections
import weakref

# this is our fake storage mechanism
_pages = weakref.WeakKeyDictionary()


class PageSequence(collections.MutableSequence):
    """
    This is an example of where abstractions leak...and so can memory!
    """
    def __init__(self, book):
        self.book = book

    def __len__(self):
        return len(retrieve_pages(self.book))

    def append(self, page):
        store_page(self.book, page)

    def insert(self, index, value):
        retrieve_pages(self.book).insert(index, value)

    def __getitem__(self, index):
        return retrieve_pages(self.book)[index]

    def __setitem__(self, index, value):
        retrieve_pages(self.book)[index] = value

    def __delitem__(self, index):
        del retrieve_pages(self.book)[index]

    def __eq__(self, other):
        return retrieve_pages(self.book) == other


def store_page(book, page):
    """
    Store a page in our fake storage
    :param book: the Book to use as index in our storage
    :param page: the Page for the Book
    :return: None
    """
    if book in _pages:
        _pages[book].append(page)
    else:
        _pages[book] = [page]


def retrieve_pages(book):
    """
    Retrieve pages from a stored Book
    :param book: instance of Book to use when looking up Page list
    :return: list of Page's for the Book, [] if Book is not found
    """
    if book in _pages:
        return _pages[book]
    return []
