#!/usr/bin/env python

import objgraph

class Animal(object):
    kingdom = 'animalia'

    def __init__(self, genus):
        self.genus = genus


class Dog(Animal):

    def __init__(self, name):
        super().__init__('Canis')
        self.name = name


dog = Dog('Maple')

objgraph.show_refs([dog])
