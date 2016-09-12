"""
A Book
"""
import collections
from .page import Page


class PageSequence(collections.MutableSequence):
    """
    See if this silly design leaks.
    """
    def __init__(self, book):
        self._book = book
        self.instances = []

    def __del__(self):
        for thing in self.instances:
            thing = None

    def __len__(self):
        return len(self.instances)

    def append(self, page):
        return self.instances.append(page)

    def insert(self, index, value):
        return self.instances.insert(index, value)

    def __getitem__(self, index):
        return self.instances[index]

    def __setitem__(self, index, value):
        return self.__delitem__(index, value)

    def __delitem__(self, index):
        return self.instances.__delitem__(index)

    def __eq__(self, other):
        return self.instances == other


class Book(object):
    """
    This book type is ok. No leaks!
    """

    def __init__(self, title=None):
        self.title = title
        self.pages = []

    def append(self, page):
        self.pages.append(page)

    def add_page(self, text):
        self.pages.append(Page(text=text))

    def __len__(self):
        return len(self.pages)




class LeakyBook(object):
    """
    This book type is leaky :-(
    """

    def __init__(self, title=None):
        self.title = title
        self.pages = PageSequence(self)

    def append(self, page):
         self.pages.append(page)

    def add_page(self, text):
        self.pages.append(Page(text=text, book=self))

    def __len__(self):
        return len(self.pages)
