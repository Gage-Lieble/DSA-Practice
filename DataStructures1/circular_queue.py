# CIRCULAR QUEUE DATA STRUCTURE
'''
- https://www.programiz.com/dsa/circular-queue
- Acts like simple queue however when rear gets to end it restarts at index 0
- Applications
    1. CPU scheduling
    2. Memory management
    3. Traffic management
'''

class CircularQueue():
    def __init__(self, k):
        self.k = k # length
        self.queue = [None] * k # array
        self.head = -1 # front
        self.tail = -1 # rear
    
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("It's full! ")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
    
    def dequeue(self):
        if (self.head == -1):
            print("It's empty! ")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
        
    def showQueue(self):
        if (self.head == -1):
            print('Empty! ')
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else: 
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

q = CircularQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print('Original Circular Queue')
q.showQueue()

q.dequeue()
q.dequeue()
print('New Circular Que after dequeue')
q.showQueue()