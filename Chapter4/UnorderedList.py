from Node import Node

class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        if self._size == 0:
            self.tail = temp
        self._size += 1
    
    def size(self):
        return self._size

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            #raise ValueError("{} is not in the list".format(item))
            print("{} is not in the list".format(item))
            return None
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        self._size -= 1
    
    def __str__(self):
        current = self.head
        string = []
        while current is not None:
            string.append("- {}".format(current.data))
            current = current.next
        return '\n'.join(string)
    
    def append(self, item):
        temp = Node(item)
        self.tail.set_next(temp)
        self.tail = temp
        self._size += 1
        
    def insert(self, index, item):
        if index == 0:
            self.add(item)
        elif index >= self.size() - 1:
            self.append(item)
        else:
            current_index = 0
            current = self.head
            while current_index != index:
                previous = current
                current = current.next
                current_index += 1
            temp = Node(item)
            temp.set_next(current)
            previous.set_next(temp)

    def index(self, item):
        
        if self.is_empty():
            print("List is empty")
            return None

        tracker = 0
        current = self.head
        while current.data != item:
            current = current.get_next()
            if current:
                tracker += 1
            else:
                print("Item not found")
                return None
        return tracker

    def pop(self, index):
        if self.is_empty():
            print("List is empty")
            return None
        current = self.head
        if index == 0:
            self.head = current.next
            return current.data
        elif index > self.size():
            print("Out of range")
            return None
        else:
            for _ in range(index):
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            return current.data
            
        

    
if __name__ == '__main__':
    x = UnorderedList()
    x.add(3)
    x.add(5)
    x.add('fly')
    x.append('key')
    x.remove(2)
    x.remove(5)
    x.insert(1, 200)
    print(x.index("io"))
    print(x.pop(3))
    print(x)