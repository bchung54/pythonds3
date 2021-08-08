from Node import Node

class QueueDLL:
    """
    Programming Exercise 4.27.7
    Queue implementation as a doubly linked list for O(1) average performance of enqueue and dequeue
    """

    def __init__(self):
        """Create new queue"""
        self._sentinel = Node("X")
        self._size = 0

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._size)

    def enqueue(self, item):
        """Add an item to the queue"""
        x = Node(item)

        if self.is_empty():
            self._sentinel.set_next(x)
            self._sentinel.set_prev(x)
        else:
            self._sentinel.prev.set_next(x)
            x.set_prev(self._sentinel.get_prev())
            self._sentinel.set_prev(x)

        self._size += 1

    def dequeue(self):
        """Remove an item from the queue"""

        output = self._sentinel.get_next()
        self._sentinel.set_next(output.get_next())
        self._size -= 1
        return output


    def size(self):
        """Get the number of items in the queue"""
        return self.size

if __name__ == '__main__':
    q = QueueDLL()
    q.enqueue(3)
    q.enqueue("boot")
    q.enqueue(9)
    print(q.dequeue().get_data())
    print(q.dequeue().get_data())
    q.enqueue(1)
    print(q.dequeue().get_data())
