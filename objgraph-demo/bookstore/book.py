"""
A Book
"""


class Book(object):

    def __init__(self, title=None):
        self.title = title
        self.pages = []

    def append(self, page):
        self.pages.append(page)

    def __len__(self):
        return len(self.pages)