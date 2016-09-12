"""
A Book
"""


class Book(object):
    """
    This book type is ok. No leaks!
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
    This book type is leaky :-(
    """

    def __init__(self, title=None):
        self.title = title
        self.pages = []

    def append(self, page):
        self.pages.append(page)

    def __len__(self):
        return len(self.pages)