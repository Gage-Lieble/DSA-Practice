# DEQUE DATA STRUCTURE
'''
- Double ended queue that can accept insertions/removal from either end
- Applications:
    1. Store browser history
    2. Undo operations in software (e.g. "ctrl+z")
'''

class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addRear(self, item):
        self.items.append(item)
    def addFront(self,item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
d = Deque()
print(f"Empty: {d.isEmpty()}")
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.items, '---')
print(f"Size: {d.size()}")
print(f"Empty: {d.isEmpty()}")
d.addRear(11)
print(d.items, '---')
print(f"Removed Rear val: {d.removeRear()}")
print(f"Removed Front val: {d.removeFront()}")
print(d.items, '---')
d.addFront(55)
d.addRear(45)
print(d.items, '---')