"""
A Page...typically in a Book!
"""
import weakref


class DumbMixin(object):

    def __init__(self, book):
        if book:
            self.book = weakref.ref(book)

    @property
    def my_ref(self):
        return self.book


class Page(DumbMixin):
    """
    Just a page in a Book, most likely.
    """

    def __init__(self, text=None, book=None):
        self.text = text
        super(Page, self).__init__(book)

