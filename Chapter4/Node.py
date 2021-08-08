class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None
        self._prev = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def get_prev(self):
        """Get previous node"""
        return self._prev

    def set_prev(self, node_prev):
        """Set previous node"""
        self._prev = node_prev

    prev = property(get_prev, set_prev)


    def __str__(self):
        """String"""
        return str(self._data)