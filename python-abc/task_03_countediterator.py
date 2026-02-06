#!/usr/bin/env python3
class CountedIterator:
    """Iterator wrapper that counts the number of items iterated"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # raises StopIteration automatically
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far"""
        return self.count

    def __iter__(self):
        """Iterator protocol requires __iter__ to return self"""
        return self
