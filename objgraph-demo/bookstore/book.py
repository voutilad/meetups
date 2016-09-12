"""
A Book
"""
from .storage import *


class Book(object):
    """
    This book type is OK. No leaks! Simple and memory based.
    """

    def __init__(self, title=None):
        self.title = title
        self.pages = []

    def append(self, page):
        self.pages.append(page)

    def __len__(self):
        return len(self.pages)


class LeakyBook(object):
    """
    This book type allegedly scales by using special 'storage' via our little
    PageSequence class. Unfortunately, it leaks!
    """

    def __init__(self, title=None):
        self.title = title
        self.pages = PageSequence(self)

    def append(self, page):
        page.book = self
        self.pages.append(page)

    def __len__(self):
        return len(self.pages)
