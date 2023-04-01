class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        # return True if self.size == 0 else False
        return True if not self.head else False

    def enqueue(self, data): 
        self.size+=1      
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def dequeue(self):
        if not self.isEmpty():
            self.size-=1
            old = self.head
            data = self.head.data
            self.head = self.head.next
            del old

        return data


q = Queue()
print(q.getSize())
q.enqueue("5")
q.enqueue(10)
q.enqueue(15)
print(q.getSize())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


'''   
    def dequeu(self):
        return
    
    def show(self):
        return
    
    def exist(self):
        return
    
    def getFirst(self):
        return
    
    def getLast(self):
        return
'''


