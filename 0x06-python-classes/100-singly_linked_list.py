#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, self.__head)
            return
        new = Node(value, self.__head)
        self.__head = new

    def __str__(self):
        list1 = []
        holder = self.__head
        while holder is not None:
            list1.append(holder.data)
            holder = holder.next_node
        list1.sort()
        return '\n'.join(str(i) for i in list1)
