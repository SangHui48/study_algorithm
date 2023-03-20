class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr

    def insertAt(self,pos, newNode):
        if pos < 0 or pos > self.nodeCount + 1:
            return False
        prev= self.getAt(pos-1)
        return self.insertAfter(prev, newNode)


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result
    
    def popAfter(self, prev):
        if prev == self.tail:
            return None
        target = prev.next
        prev.next = target.next
        target.next.prev = prev
        self.nodeCount -= 1
        return target.data
        

    def popBefore(self, next):
        if next == self.head:
            return None
        target = next.prev
        next.prev = target.prev
        target.prev.next = next
        self.nodeCount -= 1
        return target.data
        

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        if pos == 1:
            return self.popAfter(self.head)
        else:
            return self.popAfter(self.getAt(pos-1))


a = Node(5)
b = Node(3)
c = Node(2)
l = DoubleLinkedList()
l.insertAt(1, a)
l.insertAt(2, b)
l.insertAt(3, c)
print(l.traverse())
print(l.reverse())