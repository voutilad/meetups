# objgraph-demo

Example of a memory leak in Python due to leaky abstractions. It uses 
the [objgraph](https://objgraph.readthedocs.io) module to demonstrate 
finding leaks graphically or programatically.

Unit tests (in `tests` package) are provided to show simple usage of 
`objgraph` as well as show how to manually test a leak.

See the accompanying [presentation material](./presentation) for the 
talk to learn more. 

# Data Model

The project provides a Python module called `bookstore` that provides
an implementation of "book" data types. One is simple and doesn't leak 
while the other is more complex and has a memory leak intrinsic to the
(poor) design.

## Book

Simple data type. No leak. 

```
from bookstore import Book, Page
book = Book(title='Cooking with Leeks')
book.append(Page(text='Chapter 1: Making Leaks work for You'))
```

## LeakyBook

More complex data type. Similar to `Book`, but the abstraction of how
`Page`s are stored results in a leak. This is pretending there's some
storage layer that was poorly implemented.

```
from bookstore import LeakyBook, Page
book = LeakBook(title='Cooking with Leeks')
book.append(Page(text='Chapter 1: Making Leaks work for You'))
```

## Page

Represents a page in a book. Super simple, one attribute (`text`)
 
```
from bookstore import Page
page = Page(text='This is my page text')
```


# Running the Tests

To run tests, simply execute:
```
python setup.py test
```

It uses `pytest`, so you can also invoke that as an alternative.

# Copyright / License

See [../LICENSE](../LICENSE) for any copyright or license notices. The 
materials are provided as-is and certain graphics/clip-art in the 
presentation might be licensed differently.
