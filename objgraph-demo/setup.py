from setuptools import setup

setup(
    name='objgraph-demo',
    version='0.1.0',
    packages=['bookstore'],
    url='https://github.com/voutilad/meetups',
    license='MIT',
    author='Dave Voutila',
    author_email='voutilad@gmail.com',
    description='Example of using Objgraph',
    setup_requires=['pytest-runner',],
    tests_require=['pytest',],
)
