class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#LIFO = Last input first output
#UEPS = Ultima en entrar, Primera en salir
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def getData(self): 
        return self.head.data
    
    
    def isEmpty(self):
        return True if self.size == 0 else False
        #return self.size is None
    
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self): 
        data = None    
        #if self.head is self.isEmpty():
        #   return None
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            
        return data

    def getSize(self):
        return self.size
    
    def peek(self):
        #self.head.data
        if not self.isEmpty():
            return self.head.data
        else:
            return None
    
    def show(self):
        if not self.isEmpty():
            pila = ""
            elemento = self.head
            
            for i in range(0, self.size):
                pila = pila + str(elemento.data + " ")
                elemento = elemento.next
            return pila
    
    def exist(self, value):
        value = str(value)
        elemento = self.head
        for i in range(0, self.size):
            if self.isEmpty():
                return False
            elif elemento.data == value:              
                return True
            elemento = elemento.next
        else: 
            return False

'''
stack = Stack()

stack.push("Jesus")
stack.push("Maria")
stack.push("Jose")

print('El elemento es ', stack.getData())

stack.pop()
stack.pop()

print("Tamaño de ", stack.getSize())
#stack.pop()
print(stack.getData())
print("----------------------------------")
'''
'''
q1 = Stack()

print(q1) # Direccion
print(q1.head) # Direccion
print(q1.getSize())
print(q1.isEmpty())

q1.push("Jesus")
q1.push("Maria")

print(q1.getData())

q2 = Node()
print(q2.next.data)
print(q2.data)
'''

p1 = Stack()

p1.push("Jesus")
p1.push("Maria")
p1.push("Jose")

#print("Sacar")
#print(p1.pop())
#print(p1.pop())
#print(p1.pop())
#print(p1.pop())

print(p1.peek())
print(p1.getSize())
print(p1.show())
print(p1.exist("Jesuxczcs"))
print(p1.exist("Maria"))
print(p1.exist("Jose"))

