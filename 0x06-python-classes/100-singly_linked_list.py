#!/usr/bin/python3
"""SLL PROGRAM"""


class Node:
    """Class Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SLL"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        current = self.__head
        if current.data > value:
            new_node.next_node = current
            self.__head = new_node
            return

        while current.next_node:
            if current.next_node.data > value:
                break
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        node_to_list = []
        current = self.__head
        while current is not None:
            node_to_list.append(current.data)
            current = current.next_node
        return "%s" % ('\n'.join(str(i) for i in node_to_list))
