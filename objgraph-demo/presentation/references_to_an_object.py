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

kennel = [dog, Dog('Rover'), Dog('Fido')]

objgraph.show_backrefs([dog])
