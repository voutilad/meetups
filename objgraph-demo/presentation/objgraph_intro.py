#!/usr/bin/env python
import objgraph

class Monkey(object):
    pass

m1, m2 = Monkey(), Monkey()

print('Monkeys: {}'.format(objgraph.by_type('Monkey')))

del m1
del m2

print('Monkeys: {}'.format(objgraph.by_type('Monkey')))
