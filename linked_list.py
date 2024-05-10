from node import Node
import time

class LinkedList:
    head: Node = None
    size = 0
    length = 0
    def insert(self, newValue: any):
        newNode = Node(newValue, self.head)
        # newNode = Node
        # newNode.nextNode = self.head
        # newNode.value = value
        self.head = newNode
        print(self.head.value, self.head.nextNode)
        self.length += 1
    def append(self, newValue):
        if self.head == None:
            return None
    def getSize(self):
        return self.length
    def __str__(self) -> str:
        values = ''
        aux = self.head
        while aux is not None:
            values += f'{aux.value}, '
            aux = aux.nextNode
        if not values:
            return 'empty list'
        return values
    def __sizeof__(self) -> int:
        return self.length
    

l = LinkedList()
l.insert(45)
l.insert(453)
l.insert(453)
l.insert(45323)
l.insert(4512)
print(l.getSize())
print(l)