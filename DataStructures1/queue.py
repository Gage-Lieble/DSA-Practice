# QUEUE DATA STRUCTURE
'''
- Acts like waiting in line FIFO or first come first serve
- Applications:
    1. CPU/DISK scheduling
    2. Data transmission synchronization
    3. Call center phone queues (callers waiting list)
'''

class Queue:

    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def display(self, msg):
        print(f'{msg}: {self.queue}')
    
    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display('Original Queue')

for x in range(0, 2):
    q.dequeue()


q.display('New Queue after dequeue')