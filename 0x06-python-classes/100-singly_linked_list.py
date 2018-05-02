#!/usr/bin/python3
class Node
    def __init__(self, data, next_node=None)
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
            if isinstance(value, int):
                self.__data = value
            else:
                raise TypeError('data must be an integer')
    @property
    def next_node(self):
        return next_node.__data
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList
    def __init__(self)
        self.__head = None
    def sorted_insert(self, value):
        if self.__head == None
            self.data = value
            if self.
    def __str__(self)
        if len(self) = None



