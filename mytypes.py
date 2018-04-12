"""
exercisin'
"""


class _LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.link = None


class LinkedList(object):
    def __init__(self, *args):
        self._head = None
        self._len = 0
        for val in args:
            self.append(val)

    def append(self, val):
        self._len += 1

        if self._head is None:
            self._head = _LinkedListNode(val)
            return

        node = self._head
        while node.link is not None:
            node = node.link

        node.link = _LinkedListNode(val)

    def extend(self, linked_list):
        if len(linked_list) == 0:
            return

        if self._head is None:
            node = None
        else:
            node = self._head
            while node.link is not None:
                node = node.link

        for val in linked_list:
            if node is None:
                self._head = _LinkedListNode(val)
                node = self._head
                continue
            node.link = _LinkedListNode(val)
            node = node.link
        self._len += len(linked_list)

    def clear(self):
        self._head = None
        self._len = 0

    def __iter__(self):
        if self._head is None:
            raise StopIteration

        node = self._head
        while True:
            yield node.val
            if node.link is None:
                break
            node = node.link
        raise StopIteration

    def __len__(self):
        return self._len

    def _nth_node(self, n):
        node = self._head
        while n > 0:
            if node is None:
                raise IndexError("index out of range")
            node = node.link
            n -= 1

        if node is None:
            raise IndexError("index out of range")
        return node

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("list indices must be integer")
        if index < 0:
            raise NotImplemented("later")

        return self._nth_node(index).val

    def __setitem__(self, index, val):
        if not isinstance(index, int):
            raise TypeError("list indices must be integer")
        if index < 0:
            raise NotImplemented("later")
        self._nth_node(index).val = val

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("list indices must be integer")
        if index < 0:
            raise NotImplemented("later")

        if index == 0:
            if self._head is None:
                raise IndexError("index out of range")
            self._head = self._head.link
        else:
            prev_node = self._nth_node(index - 1)
            if prev_node.link is None:
                raise IndexError("index out of range")
            prev_node.link = prev_node.link.link

        self._len -= 1
